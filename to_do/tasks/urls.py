from django.urls import path
from .views import *


urlpatterns = [
    path("",Addtask.as_view(),name='home'),
    path("<int:pk>/",complete,name='completed'),
    path("search/",search,name='search')
]