from django.db import models
from django.contrib.auth.models import User


class TaskGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return f"{self.id}: {self.name}"


class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="user_tasks")

    def __str__(self):
        return f"{self.user.id}: {self.task.id}"
