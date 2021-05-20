from django import forms
from django.db import models
from django.db.models import fields
from .models import To_Do_Tasks

class ToDoForm(forms.ModelForm):
    class Meta:
        model = To_Do_Tasks
        fields = ('name','description')
