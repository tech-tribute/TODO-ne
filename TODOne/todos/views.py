from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def todo_detail(request: HttpRequest):
    return HttpResponse("Developing ...")


def edit_todo(request: HttpRequest):
    return HttpResponse("Developing ...")


def delete_todo(request: HttpRequest):
    return HttpResponse("Developing ...")
