from django.urls import path
from .views import todo_list, todo_detail

app_name = 'todos'

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('<int:pk>', todo_detail, name='todo_detail'),
]