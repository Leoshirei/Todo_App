from django.shortcuts import render, get_object_or_404, redirect

from .forms import TodoForm
from .models import Todo
# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(owner = request.user)
    return render(request, "todo/todo_list.html", {"todos": todos})

def is_completed(request, id):
    todo = get_object_or_404(Todo, id = id, owner = request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id = id, owner = request.user)
    todo.delete()
    return redirect('todo_list')

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


