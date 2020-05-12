from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/consoles
    path('', views.index, name="console-index"),
    path('<int:id>', views.get_console_by_id, name="console_details")
]