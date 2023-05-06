from rest_framework import serializers
from .models import TaskGroup, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name"]


class TaskGroupSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)

    class Meta:
        model = TaskGroup
        fields = ["id", "name", "tasks"]
