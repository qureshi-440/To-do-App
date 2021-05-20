from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,ListView
from .models import To_Do_Tasks
from .forms import ToDoForm
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.urls import reverse_lazy
import datetime
from .filter import Searchfilter
# Create your views here.

def home(request):
    return render(request,'home.html')

class Addtask(LoginRequiredMixin,CreateView):
    model = To_Do_Tasks
    form_class = ToDoForm
    template_name = 'home.html'
    success_url = reverse_lazy("tasks:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.name = self.request.POST['name']
        form.instance.description = self.request.POST['description']
        form.instance.date = self.request.POST['date']
        form.instance.starts = self.request.POST['starts']
        form.instance.ends = self.request.POST['ends']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_tasks'] = To_Do_Tasks.objects.filter(user=self.request.user,completed=False).exclude(date__lte=datetime.date.today())
            context['completed_tasks'] = To_Do_Tasks.objects.filter(user=self.request.user,completed=True)
            context['today_tasks'] = To_Do_Tasks.objects.filter(user=self.request.user,date=datetime.date.today())
            context['filter'] = Searchfilter(self.request.GET,queryset=To_Do_Tasks.objects.filter(user=self.request.user))
            context['search_results'] = Searchfilter(self.request.GET,queryset=To_Do_Tasks.objects.filter(user=self.request.user)).qs
            context['incomplete'] = To_Do_Tasks.objects.filter(user=self.request.user,date__lt=datetime.date.today(),completed=False)
        return context

def complete(request,pk):
    task = get_object_or_404(To_Do_Tasks,user=request.user,id=pk)
    task.completed = True
    task.note = request.POST["note"]
    task.satisfaction_level = request.POST["slider"]
    task.save()
    return HttpResponseRedirect(reverse_lazy("tasks:home"))

def search(request):
    queary = request.GET['search']
    results = To_Do_Tasks.objects.filter(name__icontains=queary)
    context = {'results':results}
    return render(request,'home.html',context)
