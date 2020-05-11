from django.shortcuts import render

consoles = [
    {'name': 'Playstation 4', 'price': 200},
    {'name': 'Xbox', 'price': 250}
]
# Create your views here.
def index(request):
    return render(request, 'console/index.html', context={ 'consoles': consoles })