from rest_framework import generics, permissions
from .serializers import UserSearlizer
from .models import User

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSearlizer
    permission_classes = [permissions.AllowAny]

class CheckUser(generics.ListAPIView):
    serializer_class = UserSearlizer

    def get_queryset(self):
        queryset = User.objects.filter(name=self.kwargs['name'])
        return queryset



