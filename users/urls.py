from django.urls import path
from . import views  

urlpatterns =[
    path('user_create/', views.CreateUser.as_view(), name='user_create'),
    path('users/<name>', views.CheckUser.as_view(), name ='users'),

]