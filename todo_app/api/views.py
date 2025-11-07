from rest_framework import generics 
from .serializers import TodoSerializer
from todo_app.models import Todo


class TodoListCreateView(generics.ListCreateAPIView):

    """
    View for list all todos and create a new todo.
    
    - GET: List all todos.
    - POST: Create a new todo item.
    """

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    