from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

#Login/Logout/Register
def login_todo(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todo_list')
    else:
        form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form': form})

@login_required
def logout_todo(request):
    logout(request)
    return redirect('login')

def register_todo(request):
    if request.method == "POST":
        user =  UserCreationForm(request.POST)
        if user.is_valid():
            user = user.save()
            login(request, user)
            return redirect('todo_list')
    else:
        user = UserCreationForm()
    return render(request, 'todo/register.html', {'form': user})

#Manipulate ToDo
@login_required
def todo_list(request):
    todos = Todo.objects.filter(owner = request.user)
    return render(request, "todo/todo_list.html", {"todos": todos})

@login_required
def is_completed(request, id):
    todo = get_object_or_404(Todo, id = id, owner = request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id = id, owner = request.user)
    todo.delete()
    return redirect('todo_list')

@login_required
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit = False)
            todo.owner = request.user
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form': form})

@login_required
def todo_update(request, id):
    todo = get_object_or_404(Todo, id = id, owner = request.user)
    if request.method == "POST":
        form = TodoForm(request.POST, instance = todo)
        if form.is_valid():
            todo = form.save(commit = False)
            todo.owner = request.user
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance = todo)
        return render(request, 'todo/todo_create.html', {'form': form})



