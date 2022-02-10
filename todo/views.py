from django.shortcuts import render, HttpResponse

# Create your views here.
def get_todo(request):
    return render(request, 'todo/todo_list.html')