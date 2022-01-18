from django.urls import path  # path in urls file in django directory
from . import views  # views in current directory

# path('', views.index) : when client approach default URL(serverIP:8000), execute function 'index()' in views.py
urlpatterns = [
	path('', views.index, name='index'),
# execute funtion createTodo() in views

	path('createTodo', views.createTodo, name='createTodo'),
	path('doneTodo', views.doneTodo, name='doneTodo'),
]
