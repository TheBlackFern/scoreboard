from django.urls import path
from .views import TaskGroupList

urlpatterns = [
    path("taskgroups/", TaskGroupList.as_view(), name="taskgroup-list"),
]
