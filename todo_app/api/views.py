from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics, mixins
from rest_framework.generics import GenericAPIView
from .serializers import TodoSerializer
from todo_app.models import Todo


class TodoListCreateView(generics.ListCreateAPIView):

    """
    View for list all todos and create a new todo.

    - GET: List all todos with optional searching by title and description and filtering by status.
    - POST: Create a new todo item.
    """

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['title', 'description']


class SingleTodoView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):

    """
    View for retrieving, updating, and deleting a single todo item.

    - GET: Retrieve a todo item by ID.
    - PATCH: Update a todo item partially by ID.
    - DELETE: Delete a todo item by ID.
    """

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
