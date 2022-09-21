from django.urls import path
from .views import (
    todo_list, 
    todo_detail,
    todo_create,
    todo_update
)

app_name = 'todos'

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('<int:pk>/', todo_detail, name='todo_detail'),
    path('create/', todo_create, name='todo_create'),
    path('<int:pk>/update/', todo_update, name='todo_update')
]