from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse_lazy,reverse

# Create your models here.
User = get_user_model()
class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    budget_allocated = models.PositiveIntegerField()
    completion = models.DateField()

    def save(self,*args,**kwargs) -> None:
        self.slug = slugify(self.name)
        return super().save(*args,**kwargs)

    def __str__(self) -> str:
        return self.name

class Categories(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    add = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.add + "  --" + str(self.project)

class Expenses(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    expense = models.DecimalField(max_digits=10,decimal_places=3,default=0)
    # category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    name = models.CharField(max_length=225)

    def get_absolute_url(self):
        return reverse("budget:detail",kwargs={'slug':self.project.slug})
