from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    return render(request, "todo/todo_list.html")
