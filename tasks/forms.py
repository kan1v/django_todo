from django import forms
from .models import Task
from django.utils.text import slugify

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date', 'user_from']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            })
        }
        labels = {
            'title': 'Заголовок задачи',
            'description': 'Описание задачи',
            'due_date': 'Дедлайн',
            'priority': 'Приоритет'
        }

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user is not None:
            instance.user_from = user
        if not instance.slug:
            instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance
        