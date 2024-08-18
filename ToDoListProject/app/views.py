from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm

def todo_list_view(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'todo_items': todo_items})

def add_todo_item_view(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list_view')
    else:
        form = TodoItemForm()
    return render(request, 'add_todo_item.html', {'form': form})

def delete_todo_item_view(request, pk):
    todo_item = TodoItem.objects.get(pk=pk)
    todo_item.delete()
    return redirect('todo_list_view')