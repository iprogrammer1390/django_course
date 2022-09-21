from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, "todo/todo_list.html", context)


def todo_detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todo/todo_detail.html', context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'todo/todo_create.html', context)


def todo_update(request, pk):
    todo = Todo.objects.get(pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'todo/todo_update.html', context)


