from django.db import models


status_choices = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
]


class Todo(models.Model):

    """
    Model representing a to-do item.

    Attributes:
        title (str): The title of the todo item.
        description (str): A detailed description of the todo item.
        status (str): The current status of the to-do item, chosen from predefined options (pending, in_progress, completed).
    """

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(choices=status_choices, default='pending')

    def __str__(self):
        return self.title
