from django.urls import path


app_name = 'lists'
# Create your urls here.

urlpatterns = [
    # Show lists
    path(route="", view=..., name="list_overview"),

    # Create
    path(route="add/", view=..., name="create_list"),

    # Show detail todos and detail of a list
    path(route="<int:list_id>/", view=..., name="list_detail"),
  
    # Edit name
    path(route="<int:list_id>/edit/", view=..., name="edit_list"),
    
    # Delete 
    path(route="<int:list_id>/delete/", view=..., name="delete_list"),
]
