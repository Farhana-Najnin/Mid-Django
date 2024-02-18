from typing import Any
from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def userSignUp(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account Created Successful' )
            return redirect('login')
    else:
        signup_form = SignUpForm()
    return render(request,'signup.html', {'form':signup_form})

#class based views
class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request,'Logged In successfully!!!!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Information invalid')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    

class UserLogoutView(LogoutView):
    success_url = reverse_lazy('home_page')
    def get_success_url(self):
        return self.success_url

@login_required
def UserProfile(request):
    user = request.user
    return render(request,'profile.html', {'user': user})
    
@login_required
def editProfile(request):
    if request.method == "POST":
        new_form = forms.ChangeUserData(request.POST, instance=request.user)
        if new_form.is_valid():
            new_form.save()
            messages.success(request, 'Profile Updated Successfully!!!')
            return redirect('profile')
    else:
        new_form = forms.ChangeUserData(instance = request.user)
    return render(request,'edit.html', {'form' : new_form })