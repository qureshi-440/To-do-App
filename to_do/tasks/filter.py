from django.db.models import fields
import django_filters
from .models import *

class Searchfilter(django_filters.FilterSet):
    class Meta:
        model = To_Do_Tasks
        fields = ("name",'description','date')