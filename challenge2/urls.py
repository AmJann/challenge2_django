from django.urls import path
from . import views  

urlpatterns =[
    path('todos/<int:id>', views.ToDosProtected.as_view(), name ='todos'),
    path('todo_create/', views.ToDoCreateProtected.as_view(), name='todo_create'),
    path('todo_create', views.ToDoUpdateDeleteProtected.as_view(), name='view_todo'),
    path('todo_update/<uuid:pk>/', views.ToDoUpdateDeleteProtected.as_view(), name='todo_update'),
    path('todo_delete/<uuid:pk>/', views.ToDoUpdateDeleteProtected.as_view(), name='todo_delete'),
    path('update_progress/<uuid:pk>/', views.ToDoUpdateDeleteProtected.as_view(), name='update_progress'),
    path('view_user/<uuid:pk>/', views.UserViewSet.as_view(), name='view_user'),
]