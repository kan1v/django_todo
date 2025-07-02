from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description' ,'user_from', 'is_completed', 'created_at', 'due_date']
    list_filter = ['is_completed', 'created_at', 'due_date', 'user_from']
    search_fields = ['title', 'user_from']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['is_completed', 'created_at']

