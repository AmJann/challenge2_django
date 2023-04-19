from rest_framework import serializers
from .models import ToDo
from django.contrib.auth.models import User

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('uuid','title','description', 'date_due','in_progress', 'complete','user')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'is_superuser')