from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/manufacturers
    path('', views.index, name="manufacturer-index"),
    path('<int:id>', views.get_manufacturer_by_id, name="manufacturer_details")

]