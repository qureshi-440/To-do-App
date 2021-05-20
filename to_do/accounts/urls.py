from os import name
from django.urls import path
from django.contrib.auth import views as pre_views
from .views import *

urlpatterns = [
    path("login/",pre_views.LoginView.as_view(template_name='login.html'),name='login'),
    path("logout/",pre_views.LogoutView.as_view(),name='logout'),
    path("register/",register.as_view(),name='register'),
    path("verify/<user>/",verify_email,name='verify')
]