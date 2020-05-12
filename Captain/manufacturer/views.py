from django.shortcuts import render
from manufacturer.models import Manufacturer
# Create your views here.
def index(request):
    return render(request, 'manufacturer/index.html', context={'manufacturers': Manufacturer.objects.all().order_by('name')})
