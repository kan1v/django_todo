from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('task-list/', views.tasks_list, name='task_list'),
    path('task_form/', views.task_form, name='task_form'),
    path('task/<slug:slug>/edit', views.task_edit, name='task_edit'),
    path('task/<slug:slug>/delete', views.task_delete, name='task_delete'),
    path('task/complete/', views.task_complete, name='task_complete'),
    path('task-list/task-detail/<slug:slug>/', views.task_detail, name='task_detail'),
]