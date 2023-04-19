from django.urls import path
from . import views  

urlpatterns =[
    path('user_create/', views.CreateUser.as_view(), name='user_create'),
]