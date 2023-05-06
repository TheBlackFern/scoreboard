from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, TaskGroup
from .serializers import TaskGroupSerializer


class TaskGroupList(generics.ListAPIView):
    queryset = TaskGroup.objects.all()
    serializer_class = TaskGroupSerializer
