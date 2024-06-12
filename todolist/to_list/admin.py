from django.contrib import admin # type: ignore

# Register your models here.
from to_list.models import ToDoItem


admin.site.register(ToDoItem)

