from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Task, TaskGroup, UserTask
from .serializers import TaskGroupSerializer


class TaskGroupList(generics.ListAPIView):
    queryset = TaskGroup.objects.all()
    serializer_class = TaskGroupSerializer


def group_stats(group):
    group_tasks = group.tasks.all()
    total_tasks = group_tasks.count()
    user_stats = []
    for user in User.objects.all():
        completed_tasks = 0
        for task in group_tasks:
            if UserTask.objects.filter(user=user, task=task).exists():
                completed_tasks += 1
        if completed_tasks > 0:
            user_stats.append(
                {
                    "user_id": user.id,
                    "username": user.username,
                    "percentage": round(completed_tasks / total_tasks * 100, 2),
                }
            )
    return {group.id: user_stats}


class GroupTaskCompletionView(APIView):
    def get(self, request):
        groups = TaskGroup.objects.all()
        group_completion_stats = {}
        for group in groups:
            group_completion_stats.update(group_stats(group))
        return Response(group_completion_stats)


class UserTaskCompletionView(APIView):
    def get(self, request):
        users = User.objects.all()
        data = {}
        for user in users:
            user_data = {}
            user_tasks = UserTask.objects.filter(user=user)
            for user_task in user_tasks:
                task = user_task.task
                group = task.group
                task_name = task.name
                group_name = group.name
                if group_name not in user_data:
                    user_data[group_name] = {}
                user_data[group_name][task_name] = True
            for group in TaskGroup.objects.all():
                group_name = group.name
                if group_name not in user_data:
                    user_data[group_name] = {}
                for task in group.tasks.all():
                    task_name = task.name
                    if task_name not in user_data[group_name]:
                        user_data[group_name][task_name] = False
            data[user.username] = user_data
        return Response(data)


# this one is for more comfortable prototyping only
@csrf_exempt
def add_usertask(request, user_id, task_id):
    """
    Quickly make a task done for a user.
    """
    try:
        Task.objects.get(id=task_id)
        User.objects.get(id=user_id)
    except:
        return HttpResponse(status=404)
    try:
        UserTask.objects.get(user_id=user_id, task_id=task_id)
    except:
        UserTask.objects.create(user_id=user_id, task_id=task_id)
    return HttpResponse(status=200)
