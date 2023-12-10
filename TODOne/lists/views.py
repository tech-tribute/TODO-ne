from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST, require_GET

from . forms import CreateListForm
from . models import List


# Create your views here.

@require_GET
def list_overview(request:HttpRequest):
    lists = List.objects.order_by('-create_date')
    form = CreateListForm()

    context = {
        "lists":lists,
        "form":form,
    }

    return render(request=request, template_name="lists/list_overview.html", context=context)

def add_todo(request:HttpRequest):
    return HttpResponse("Developing ...")


@require_POST
def create_list(request:HttpRequest):
    form = CreateListForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        new_list = List(name=name)
        new_list.save()
        return redirect("lists:list_detail", list_id=new_list.id)

    print("HOoooooooooo")
    return redirect("lists:list_overview")

@require_GET
def list_detail(request:HttpRequest, list_id:int):
    list_ = List.objects.get(id=list_id)
    todos = list_.todos


def edit_list(request:HttpRequest):
    return HttpResponse("Developing ...")


def delete_list(request:HttpRequest, list_id:int):
    return HttpResponse("Developing ...")
