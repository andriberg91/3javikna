from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/consoles
    path('', views.index, name="console-index"),
    path('<int:id>', views.get_console_by_id, name="console_details"),
    path('console_type/<int:type_id>', views.get_console_by_type, name="console_type"),
    path('create_console', views.create_console, name="create_console"),
    path('delete_console/<int:id>', views.delete_console, name="delete_console"),
    path('update_console/<int:id>', views.update_console, name="update_console"),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart')
]