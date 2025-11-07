from django.urls import path
from .views import TodoListCreateView, SingleTodoView

urlpatterns = [
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', SingleTodoView.as_view(), name='todo-detail')
]
