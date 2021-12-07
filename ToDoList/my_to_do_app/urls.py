from django.urls import path  # path in urls file in django directory
from . import views  # views in current directory

urlpatterns = [
	path('', views.index)
]
