from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, EditTaskForm
from django.views.decorators.http import require_POST

def home_page(request):
    return render(request, 'base.html')

def about_page(request):
    return render(request, 'tasks/about.html')

def tasks_list(request):
    task_list = Task.objects.all()
    completed_tasks = Task.completed_tasks.all()
    return render(request, 'tasks/task_list.html',
                  {'task_list': task_list,
                   'completed_tasks': completed_tasks})

def task_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('tasks:task_list')
        else:
            # Для отладки ошибок можно вывести их в консоль
            print(form.errors)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})



@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('tasks:task_list')

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        edit_form = EditTaskForm(request.POST)
        if edit_form.is_valid():
            edit_form.save(user=request.user)
            return redirect('tasks:task_list')
    else:
        edit_form = EditTaskForm()
    return render(request, 'tasks/edit_task_form.html', {'edit_form': edit_form})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

