from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/frontpage
    path('', views.index, name="frontpage-index"),
]