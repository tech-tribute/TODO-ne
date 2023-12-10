from django.urls import path


app_name = "todos"
# Create your urls here.

urlpatterns = [
    # Create
    path(
        "list/<int:list_id>/add_todo/", ..., name="add_todo"
    ),
    # Read (Show detail)
    path("<int:todo_id>/", ..., name="todo_detail"),
    # Update (Edit)
    path("<int:todo_id>/edit/", ..., name="edit_todo"),
    # Delete
    path("<int:todo_id>/delete/", ..., name="delete_todo"),

    # CRUD
]
