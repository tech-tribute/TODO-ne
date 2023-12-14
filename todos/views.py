from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST, require_GET
from .models import Todo
from .forms import *


# Create your views here.
def todo_detail(request: HttpRequest, todo_id: int):
    todo = Todo.objects.get(id=todo_id)

    context = {
        "todo":todo,
    }

    return render(
        request=request,
        template_name="todos/todo_detail.html",
        context=context,
    )


def edit_todo(request: HttpRequest, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST" :
        form = EditTodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            todo.title = title
            todo.save()
            return redirect("todos:todo_detail", todo_id=todo_id)
    
    mark_as = request.GET.get("mark_as")
    if mark_as in ["complete", "uncomplete"]:
        if mark_as == "complete":
            todo.is_complete = True
        else:
            todo.is_complete = False
        todo.save()
    
    return redirect("lists:list_detail", list_id=todo.parent_list.id)



@require_GET
def delete_todo(request: HttpRequest, todo_id):
    todo = Todo.objects.get(id=todo_id)
    list_id = todo.parent_list.id
    todo.delete()
    return redirect("lists:list_detail", list_id=list_id)
