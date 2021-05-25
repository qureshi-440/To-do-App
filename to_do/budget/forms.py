from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name","description","budget_allocated")
        
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields["name"].label = "Project Name"
            self.fields['description'].label = "Description"
            self.fields["budget_allocated"].label = "Budget"
            # self.fields["completion"].label = "Completion Date"

class ExpenseForm(forms.ModelForm):
    class Meta :
        model = Expenses
        fields = ("name","expense")      