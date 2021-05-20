from django.contrib import admin
from .models import To_Do_Tasks
from django.contrib.auth import get_user_model
# Register your models here.

User = get_user_model() 

class ToDoAdmin(admin.ModelAdmin):
    list_display = ['user','name','created','completed']
    list_filter = ('completed',)
    search_fields = ('name',)


admin.site.register(To_Do_Tasks,ToDoAdmin)