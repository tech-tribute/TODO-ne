from django.urls import path
from . import views


app_name = "todos"
# Create your urls here.

urlpatterns = [
    # Read (Show detail)
    path(route="<int:todo_id>/", view=views.todo_detail, name="todo_detail"),
    # Update (Edit)
    path(route="<int:todo_id>/edit/", view=views.edit_todo, name="edit_todo"),
    # Delete
    path(route="<int:todo_id>/delete/", view=views.delete_todo, name="delete_todo"),
]
