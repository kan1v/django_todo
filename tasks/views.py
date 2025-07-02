from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home_page(request):
    return render(request, 'base.html')

def about_page(request):
    return render(request, 'tasks/about.html')

def tasks_list(request):
    task_list = Task.objects.all()
    return render(request, 'tasks/task_list.html',
                  {'task_list': task_list})

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



