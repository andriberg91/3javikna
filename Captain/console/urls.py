from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/consoles
    path('', views.index, name="console-index"),
]