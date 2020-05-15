from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from console.forms.console_form import ConsoleCreateForm
from console.forms.console_form import ConsoleUpdateForm
from console.models import Console, ConsoleImage, ConsoleType
from cart.models import CartItem, Order
from django.contrib import messages


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        consoles = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.consoleimage_set.first().image,
            'price': x.price
        } for x in Console.objects.filter(name__icontains=search_filter) ]
        return JsonResponse({ 'data': consoles })
    if 'sort_by' in request.GET:
        sort_by = request.GET['sort_by']
        consoles = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.consoleimage_set.first().image,
            'price': x.price
        } for x in Console.objects.filter(name__icontains=sort_by)]
        return JsonResponse({'data': consoles})


    context = {'consoles': Console.objects.all().order_by('name')}
    return render(request, 'console/index.html', context)

# /consoles/3

def get_console_by_id(request, id):
        return render(request, 'console/console_details.html', {
            'console': get_object_or_404(Console, pk=id)
        })
def get_console_by_type(request, type_id):
    return render(request, 'console/console_type.html', {
        'console': get_object_or_404(Console, type_id=type_id)
    })
def create_console(request):
    if request.method == 'POST':
        form = ConsoleCreateForm(data=request.POST)
        if form.is_valid():
            console = form.save()
            console_image = ConsoleImage(image=request.POST['image'], console=console)
            console_image.save()
            return redirect('console-index')
    else:
        form = ConsoleCreateForm()
    return render(request, 'console/create_console.html', {
        'form': form
    })
@login_required()
def delete_console(request, id):
    console = get_object_or_404(Console, pk=id)
    console.delete()
    return redirect('console-index')

@login_required()
def update_console(request, id):
    instance = get_object_or_404(Console, pk=id)
    if request.method == 'POST':
        form = ConsoleUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('console_details', id=id)
    else:
        form = ConsoleUpdateForm(instance=instance)
    return render(request, 'console/update_console.html', {
        'form': form,
        'id': id
    })

class OrderSummaryView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'cart/cart.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "There is nothing in basket" )
            return redirect("/")


def add_to_cart(request, id):
    product = get_object_or_404(Console, pk=id)
    order_item, created = CartItem.objects.get_or_create(product=product, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if order item is in the order
        if order.products.filter(product__name=product.name).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "Magn var uppfært")
        else:
            messages.info(request, "Vara var sett í körfu")
            order.products.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.products.add(order_item)
    messages.success(request, "Vara færð í körfu")
    return redirect('console-index')




















