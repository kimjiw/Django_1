from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index (request):
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo (request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo (content=user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("create Todo! {}".format(user_input_str))

def deleteTodo (request):
    done_todo_id = request.GET['todoNum']
    todo = Todo.objects.get(id=done_todo_id)
    todo.delete()
    #print('done todo id: {}'.format(done_todo_id))
    return HttpResponseRedirect(reverse('index'))

def doneTodo (request):
    done_todo_id = request.GET['todoNum']
    todo = Todo.objects.get(id=done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))
