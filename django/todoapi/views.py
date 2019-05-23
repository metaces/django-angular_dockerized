from .models import Task
from .serializers import TaskSerializer

from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TaskList(generics.ListCreateAPIView):
    # """
    # VIEW ALL TASKS
    # """
    # def get(self, request, format=None):
    #     task = Task.objects.all()
    #     serializer = TaskSerializer(task, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     """
    #     CREATE A TASK
    #     """
    #     serializer = TaskSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # """
    # LIST AND CREATE TASKS
    # """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    RETURNS A SINGLE TASK AND ALLOWS UPDATES AND DELETION OF A TASK
    """
    # def get_object(self, task_id):
    #     try:
    #         return Task.objects.get(pk=task_id)
    #     except Task.DoesNotExist:
    #         raise Http404
    # def get(self, request, task_id, format=None):
    #     task = self.get_object(task_id)
    #     serializer = TaskSerializer(task)
    #     return Response(serializer.data)
    # def put(self, request, task_id, format=True):
    #     task = self.get_object(task_id)
    #     serializer = TaskSerializer(task, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def delete(self, request, task_id, format=True):
    #     task = self.get_object(task_id)
    #     task.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'task_id'
