from django.contrib import admin
from .models import Todo, task_done

# Register your models here.
admin.site.register(Todo)
admin.site.register(task_done)