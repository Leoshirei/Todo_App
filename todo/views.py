from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(owner = request.user)
    return render(request, "todo/todo_list.html", {"todos": todos})

def is_completed(request, id):
    todo = get_object_or_404(Todo, id = id, owner = request.user)
    todo.completed = not todo.completed
    if todo.completed:
        todo.delete()
    else:
        todo.save()
    return redirect('todo_list')

