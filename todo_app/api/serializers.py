from rest_framework import serializers
from todo_app.models import Todo

class TodoSerializer(serializers.ModelSerializer):

    """
    Serializer for the Todo model.
    Serializes all fields of the Todo model.
    """

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'status']