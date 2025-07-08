from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, EditTaskForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def home_page(request):
    return render(request, 'base.html')

def about_page(request):
    return render(request, 'tasks/about.html')

@login_required
def tasks_list(request):
    user = request.user
    task_list = Task.objects.filter(user_from=user)
    completed_tasks = Task.completed_tasks.filter(user_from=user)
    return render(request, 'tasks/task_list.html',
                  {'task_list': task_list,
                   'completed_tasks': completed_tasks})

@login_required
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


@login_required
def task_edit(request, slug):
    task = get_object_or_404(Task, slug=slug)
    if request.method == 'POST':
        edit_form = EditTaskForm(request.POST, instance=task)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('tasks:task_list')
    else:
        edit_form = EditTaskForm(instance=task)
    return render(request, 'tasks/edit_task_form.html', {'edit_form': edit_form})

@login_required
def task_detail(request, slug):
    task = get_object_or_404(Task, slug=slug)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_complete(request):
    task_slug = request.GET.get('task_slug')
    task = get_object_or_404(Task, slug=task_slug)
    task.is_completed = True
    task.save()
    return redirect('tasks:task_detail', slug=task.slug)

@login_required
@require_POST
def task_delete(request, slug):
    task = get_object_or_404(Task, slug=slug)
    task.delete()
    return render(request, 'tasks/task_delete.html', {'task': task})