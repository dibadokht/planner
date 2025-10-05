from simpleplan.models import Task
from rest_framework.generics import ListAPIView , CreateAPIView , UpdateAPIView , DestroyAPIView 
from simpleplan.serializers import *
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

class MarkAsCompleted(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def patch(self , request , pk):
        try:
            task = Task.objects.get(pk=pk)
            task.is_completed = True
            task.save()
            
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Task.DoesNotExist:
              return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
        
class AddCategorylist(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = CategorySerializer
    
class AllCategorylist(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = CategorySerializer
    
