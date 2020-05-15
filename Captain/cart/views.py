from django.shortcuts import render
from cart.models import Cart

# Create your views here.
def index(request):
    context = {'cart': Cart.objects.all().order_by('name')}
    return render(request, 'cart/cart.html', context)


