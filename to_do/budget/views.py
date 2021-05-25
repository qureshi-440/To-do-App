from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView,UpdateView,DeleteView,DetailView,CreateView
from .models import *
from .forms import ProjectForm,ExpenseForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, request
from .utils import *
# Create your views here.

class allprojects(LoginRequiredMixin,CreateView):
    model = Project
    template_name = 'list.html'
    form_class = ProjectForm
    success_url = reverse_lazy("budget:list")

    def form_valid(self, form):
        form.instance.user =self.request.user
        form.instance.completion = self.request.POST['completion']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        def multiple():
            list = []
            projects = Project.objects.filter(user=self.request.user)
            for project in projects:
                expenses = Expenses.objects.filter(project=project)
                remaining = total_remaining(project,expenses)
                list.append(remaining)
            return(list)

        all_projects = Project.objects.filter(user=self.request.user)
        budget_remaining = multiple()
        all = zip(all_projects,budget_remaining)
        context["all"] = all
        return context

class detail(LoginRequiredMixin,DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'detail.html'

    def get_object(self, *args,**kwargs):
        obj =  super().get_object(*args,**kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Project,slug=self.kwargs["slug"])
        expenses = Expenses.objects.filter(project=project)
    
        context["expenses"] = Expenses.objects.filter(project=project)
        context["total_expense"] = total_expense(expenses)
        context["budget_remaining"] = total_remaining(project,expenses)
        return context

class expense(CreateView):
    model = Expenses
    form_class = ExpenseForm
    template_name = 'form.html'

    def form_valid(self, form,**kwargs):
        project = get_object_or_404(Project,slug=self.kwargs["slug"])
        form.instance.project = project
        # form.instance.name = form.cleaned_data["name"]
        # form.instance.expense = form.cleaned_data["cost"]
        form.save()
        return super().form_valid(form,**kwargs)

class updateexpense(UpdateView):
    model = Expenses
    form_class = ExpenseForm
    template_name = 'form.html'

    def get_object(self, *args,**kwargs):
        obj = super().get_object(*args,**kwargs)
        if obj.project.user != self.request.user:
            raise PermissionDenied()
        return obj

class deleteexpense(DeleteView):
    model = Expenses

    def delete(self, request, *args, **kwargs):
        expense_id = Expenses.objects.get(id=self.kwargs["pk"])
        project_slug = expense_id.project.slug
        expense_id.delete()
        return HttpResponseRedirect(reverse("budget:detail",kwargs={"slug":project_slug}))