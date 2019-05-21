from rest_framework import serializers

from .models import Task

class TaskSerializer(serializer.ModelSerializer):

    class Meta:

        model = Task

        fields = ('title', 'content', 'created_on', 'due_date')