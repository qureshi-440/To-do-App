from django.urls import path
from .views import *

app_name = 'budget'

urlpatterns = [
    path("",allprojects.as_view(),name='list'),
    path("<slug>/",detail.as_view(),name='detail'),
    path("expense/<str:slug>/",expense.as_view(),name='expense'),
    path("expense/update/<int:pk>/",updateexpense.as_view(),name="update_expense"),
    path("expense/delete/<int:pk>/",deleteexpense.as_view(),name="expense_delete"),
]