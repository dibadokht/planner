from django.urls import path
from simpleplan.views import AllTasklist , AddTasklist , UpdateTask , DeleteTask , MarkAsCompleted

urlpatterns = [
    path('task-list/' , AllTasklist.as_view()),
    path('add-task/' , AddTasklist.as_view()),
    path('update-task/<str:id>' , UpdateTask.as_view()),
    path('delete-task/<str:id>' , DeleteTask.as_view()),
    path('task/complete/<str:id>' , MarkAsCompleted.as_view())
    ]