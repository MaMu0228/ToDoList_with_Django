from django.db import models

### ToDoList/my_to_do_app/models.py


# Create your models here.
class Todo(models.Model):
	content = models.CharField(max_length = 255)
	# 
	isChecked = models.BooleanField(default = False)

