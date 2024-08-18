from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list_view, name='todo_list_view'),
    path('add/', views.add_todo_item_view, name='add_todo_item_view'),
    path('delete/<pk>/', views.delete_todo_item_view, name='delete_todo_item_view'),
]