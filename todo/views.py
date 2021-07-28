from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def list(request):
    return render(request,'todo/list.html')

def detail(request, todo_id):
    return HttpResponse("You're looking at todo %s." % todo_id)

@csrf_exempt
def add(request):
    response = "You're looking at the results of todo."
    return HttpResponse(response)

@csrf_exempt
def edit(request, todo_id):
    return HttpResponse("You're voting on todo %s." % todo_id)

@csrf_exempt
def delete(request, todo_id):
    return HttpResponse("You're voting on todo %s." % todo_id)
