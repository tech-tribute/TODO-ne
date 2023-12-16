from django.urls import path
from . import views


app_name = "lists"
# Create your urls here.

urlpatterns = [
    # Show lists
    path(route="", view=views.list_overview, name="list_overview"),
    # Create todo
    path(route="<int:list_id>/add_todo/", view=views.add_todo, name="add_todo"),
    # Create list
    path(route="add/", view=views.create_list, name="create_list"),
    # Show detail todos and detail of a list
    path(route="<int:list_id>/", view=views.list_detail, name="list_detail"),
    # Delete
    path(route="<int:list_id>/delete/", view=views.delete_list, name="delete_list"),
]
