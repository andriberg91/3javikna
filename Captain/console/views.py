from django.shortcuts import render , get_object_or_404
from console.models import Console

def index(request):
    context = {'consoles': Console.objects.all().order_by('name')}
    return render(request, 'console/index.html', context)

# /consoles/3

def get_console_by_id(request, id):
    return render(request, 'console/console_details.html', {
        'console': get_object_or_404(Console, pk=id)
    })