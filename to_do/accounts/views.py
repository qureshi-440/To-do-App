from django.http import request,HttpResponseRedirect,HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy,reverse
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login,get_user_model
from django.core.mail import message, send_mail,EmailMessage
from django.template.loader import get_template
# Create your views here.

class register(CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserForm
    # success_url = reverse_lazy("tasks:home")

    def form_valid(self, form):
        form.save(commit = False)
        form.is_active = False
        form.save()
       
        email = self.request.POST['email']
        password = self.request.POST['password1']

        ctx = {
            'user' :email
        }
        message = get_template('email.html').render(ctx)
        msg = EmailMessage(
            "Email verification from To Do App",
            message,
            'mohammed045farhan@gmail.com',
            [email]
        )
        msg.content_subtype = "html"
        msg.send()

        user = authenticate(email=form.cleaned_data['email'],password=form.cleaned_data['password1'])
        login(self.request,user)
        return HttpResponseRedirect(reverse("tasks:home"))
                
User = get_user_model()
def verify_email(request,user):
    person = get_object_or_404(User,email=user)
    person.is_active = True
    person.save()
    return HttpResponseRedirect(reverse("tasks:home"))
