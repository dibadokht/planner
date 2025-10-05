from simpleplan.models import Task
from rest_framework.generics import ListAPIView , CreateAPIView , UpdateAPIView , DestroyAPIView
from simpleplan.serializers import *
from rest_framework import permissions

class AllTasklist(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AddTasklist(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class UpdateTask(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class DeleteTask(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    


