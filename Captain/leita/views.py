from django.shortcuts import render, get_object_or_404
from console.models import Console
from django.http import JsonResponse

# Create your views here.
def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        consoles = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.consoleimage_set.first().image,
            'price': x.price
        } for x in Console.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': consoles})
    context = {'leita': Console.objects.all().order_by('name')}
    return render(request, 'console/index.html', context)

def get_console_by_id(request, id):
    return render(request, 'console/console_details.html', {
        'console': get_object_or_404(Console, pk=id)
    })