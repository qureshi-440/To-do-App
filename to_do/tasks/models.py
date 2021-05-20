# from accounts.models import User
import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

User = get_user_model()

class To_Do_Tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=200,null=True,blank=True)
    date = models.DateField()
    ends = models.TimeField(null=True,blank=True)
    starts = models.TimeField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    note = models.TextField(null=True,blank=True)
    satisfaction_level = models.PositiveIntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.name + "  -" + str(self.user)