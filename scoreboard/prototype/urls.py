from django.urls import path
from .views import (
    TaskGroupList,
    UserTaskCompletionView,
    GroupTaskCompletionView,
    add_usertask,
)

urlpatterns = [
    path("groups/", TaskGroupList.as_view(), name="taskgroup-list"),
    path("usercompletion/", UserTaskCompletionView.as_view(), name="userdone-stats"),
    path("groupcompletion/", GroupTaskCompletionView.as_view(), name="groupuser-stats"),
    path("<int:user_id>/<int:task_id>", add_usertask, name="user-did-task"),
]
