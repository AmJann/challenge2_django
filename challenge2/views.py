from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ToDoSerializer
from .serializers import UserSerializer
from .models import ToDo
from django.contrib.auth.models import User

class ToDosProtected(generics.ListAPIView):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        queryset = ToDo.objects.filter(user=self.kwargs['id'])
        return queryset


 

class ToDoCreateProtected(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer 
    
 

class ToDoUpdateDeleteProtected(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

class UserViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer    