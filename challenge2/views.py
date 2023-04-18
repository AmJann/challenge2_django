from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ToDoSerializer
from .models import ToDo

class ToDosProtected(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer    

    permission_classes = [permissions.IsAuthenticated]

class ToDoCreateProtected(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer 
    
    permission_classes = [permissions.IsAuthenticated]   

class ToDoUpdateDeleteProtected(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    permission_classes = [permissions.IsAuthenticated]      