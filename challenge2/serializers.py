from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ('uuid','title','description', 'date_due','in_progress', 'complete','user')