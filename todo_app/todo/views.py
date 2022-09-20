from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, "todo/todo_list.html", context)
