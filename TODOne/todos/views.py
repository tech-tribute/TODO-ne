from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST, require_GET
from . models import Todo


# Create your views here.
def todo_detail(request: HttpRequest, todo_id:int):
    return HttpResponse("Developing ...")


def edit_todo(request: HttpRequest):
    return HttpResponse("Developing ...")


@require_GET
def delete_todo(request: HttpRequest, todo_id):
    todo = Todo.objects.get(id=todo_id)
    list_id = todo.parent_list.id
    todo.delete()
    return redirect("lists:list_detail", list_id=list_id)
