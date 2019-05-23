from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer

class TaskList(generics.ListAPIView):
    """
    VIEW ALL TASKS
    """
    task = Task.objects.all()
    serializer = TaskSerializer
    