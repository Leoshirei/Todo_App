from django.urls import path
from . import views
urlpatterns = [
    path('', views.todo_list, name = "todo_list"),
    path('completed/<int:id>/', views.is_completed, name='is_completed'),
    path('<int:id>/delete/', views.todo_delete, name='todo_delete'),
    path('create/', views.todo_create, name = 'todo_create'),
    path('<int:id>/update/', views.todo_update, name = 'todo_update'),
]