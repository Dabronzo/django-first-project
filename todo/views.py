from django.shortcuts import render, redirect
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

