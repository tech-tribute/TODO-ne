from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST, require_GET

from .forms import *
from todos.forms import *
from .models import List
from todos.models import Todo


# Create your views here.


@require_GET
def list_overview(request: HttpRequest):
    lists = List.objects.order_by("-create_date")
    form = CreateListForm()

    context = {
        "lists": lists,
        "form": form,
    }

    return render(
        request=request, template_name="lists/list_overview.html", context=context
    )


@require_POST
def add_todo(request: HttpRequest, list_id:int):
    form = CreateTodoForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        parent_list = List.objects.get(id=list_id)
        new_todo = Todo(title=title, parent_list=parent_list)
        new_todo.save()

    return redirect("lists:list_detail", list_id=list_id)


@require_POST
def create_list(request: HttpRequest):
    form = CreateListForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        new_list = List(name=name)
        new_list.save()
        return redirect("lists:list_detail", list_id=new_list.id)

    return redirect("lists:list_overview")


@require_GET
def list_detail(request: HttpRequest, list_id: int):
    list_ = List.objects.get(id=list_id)
    todos: Todo = list_.todos.all()
    uncompleted_todos = todos.filter(is_complete=False)
    completed_todos = todos.filter(is_complete=True)

    filter_ = request.GET.get("filter")
    if filter_ in ["active", "completed"]:
        if filter_ == "active":
            todos = uncompleted_todos
        elif filter_ == "completed":
            todos = completed_todos

        
    context = {
        "list": list_,
        "todos": todos,
        "completed_todos": completed_todos,
        "uncompleted_todos": uncompleted_todos,
    }

    return render(
        request=request,
        template_name="lists/list_detail.html",
        context=context,
    )


@require_POST
def edit_list(request: HttpRequest, list_id=int):
    form = EditListForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        list_ = List.objects.get(id=list_id)
        list_.name = name
        list_.save()
        return redirect("lists:list_detail", list_id=list_.id)


@require_GET
def delete_list(request: HttpRequest, list_id: int):
    list_ = List.objects.get(id=list_id).delete()

    return redirect("lists:list_overview")
