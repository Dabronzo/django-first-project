from django.shortcuts import render, redirect, get_object_or_404
from .models import Itens
from .forms import ItemForm

# Create your views here.


def get_todo(request):
    items = Itens.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    """View function dor the add item page"""
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo')
        
    form = ItemForm()
    context = {
        'form': form
    }

    return render(request, 'todo/add_item.html', context)

def edit_item(request, item_id):
    """ Edit func"""
    item = get_object_or_404(Itens, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    """Toggling the done in the itens"""
    item = get_object_or_404(Itens, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo')

def delete_item(request, item_id):
    """Func to delete"""
    item = get_object_or_404(Itens, id=item_id)
    item.delete()
    return redirect('get_todo')