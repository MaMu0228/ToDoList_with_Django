from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.

def index(request):
	""" send string "my_to_do_app first page" to client"""
    	# return HttpResponse("my_to_do_app first page")

	todos = Todo.objects.all()
	content = {'todos': todos}
	
	
	"""send 'my_to_do_app/index.html' to client who sends reqeust""" 
	return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
	user_input_str = request.POST['todoContent']
	# the string 'todoContent' in POST in request sended from client
	# input in user_input_str variable
	new_todo = Todo(content = user_input_str)
	# use .models.Todo class and make new object new_todo 
	new_todo.save()
	# the new object 'new_todo' save in .models file
	return HttpResponseRedirect(reverse('index'))
	# Find url having name 'index' and Redirect to that url 
	
	# return HttpResponse("created 'Todo' =>" + user_input_str)

# '''3
def doneTodo(request):
	# if HTML used method 'GET' in '<form>', Server must use 'GET' also 
	# method 'POST' context is also same 
	done_todo_id = request.GET['todoNum']
	
	print(f"id of todo : {done_todo_id}")
	# models.todo
	# todo.content : CharField(max_length = 255)
	# todo.ischecked : BooleanField(default = False)
	# make object 'todo' from class 'Todo' having id = done_todo_id
	todo = Todo.objects.get(id = done_todo_id)
	todo.isChecked = True
	todo.save()
	# after code is done, return to homepage
	return HttpResponseRedirect(reverse('index'))	
# '''















