from django.urls import path
from simpleplan.views import AllTasklist , AddTasklist , UpdateTask , DeleteTask , MarkAsCompleted , AddCategorylist , AllCategorylist

urlpatterns = [
    path('task-list/' , AllTasklist.as_view()),
    path('add-task/' , AddTasklist.as_view()),
    path('update-task/<str:id>' , UpdateTask.as_view()),
    path('delete-task/<str:id>' , DeleteTask.as_view()),
    path('task/complete/<str:pk>' , MarkAsCompleted.as_view()),
    path('add-category/' , AddCategorylist.as_view()),
    path('category-list/' ,AllCategorylist.as_view())
    ]