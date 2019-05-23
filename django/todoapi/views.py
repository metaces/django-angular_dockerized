from .models import Task
from .serializers import TaskSerializer

from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

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
    """
    LIST AND CREATE TASKS
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    