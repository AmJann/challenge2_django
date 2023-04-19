from rest_framework import generics, permissions
from .serializers import UserSearlizer
from .models import User

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSearlizer
    permission_classes = [permissions.AllowAny]



