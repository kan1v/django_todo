from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('task-list/', views.tasks_list, name='task_list'),
    path('task_form/', views.task_form, name='task_form'),
    path('task/<int:pk>/delete', views.task_delete, name='task_delete'),
    path('task-list/task-detail/<int:pk>/', views.task_detail, name='task_detail'),
]