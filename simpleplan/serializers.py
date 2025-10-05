from rest_framework.serializers import ModelSerializer
from simpleplan.models import Category , Task

        
class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'