from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
# Create your views here.
from django.urls import reverse_lazy
from django.contrib import messages
from . forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.views.generic import CreateView,FormView
from django.contrib.auth.views import LoginView,LogoutView


@method_decorator(login_required, name = 'dispatch')
class AddMusicianView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('home_page')
    def form_valid(self, form):
        messages.success(self.request, 'Successfully added a Musician!')
        return super().form_valid(form)
        


#class based view 
class UserSignupView(FormView):
    form_class = forms.RegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self,form):
        if not self.request.user.is_authenticated:
            messages.success(self.request, 'Account created successfully!')
            form.save()
            return super().form_valid(form)
        return redirect('login')
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect('login')

#class based view login
class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = name, password = password)
            if user is not None:
                login(self.request, user)
                messages.success(self.request, 'Logged in successfully!!!!')
                return redirect('home_page')
        else:
            return redirect('signup')
        
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('signup')
        

@method_decorator(login_required , name = 'dispatch')
class UserLogoutView(LogoutView):
    def get(self,request):
        logout(request)
        messages.success(self.request, 'Logout successfully!!!!!')
        return redirect('logout')
    