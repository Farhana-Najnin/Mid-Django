from django.shortcuts import render, redirect 
from . import forms 
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required  
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
# Create your views here.

@login_required
def user_profile(request):
    return render(request, 'profile_page.html', {'type' : 'Profile'})

def user_signup(request):
    if request.method == 'POST':
        signupform = forms.SignUpForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            messages.success(request, "Signed Up Successfully")
            return redirect('home_page')
    else:
        signupform = forms.SignUpForm()
    return render(request, 'signup_page.html', {'form': signupform,'type':'Sign up'})

def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            userpass = login_form.cleaned_data['password']
            user = authenticate(username = username, password = userpass)
            if user is not None:
                messages.success(request, 'Logged in successfully')
                login(request,user)
                return redirect('user_profile')
            else:
                messages.warning(request,'Login first')
                return redirect('user_signup')
    else:
        login_form = AuthenticationForm()

    return render(request,'login_page.html', {'form': login_form, 'type': 'Login'})


def user_logout(request):
    messages.success(request,'Logged Out Successfully')
    logout(request)
    return redirect('home_page')

@login_required
def changepassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            passwordForm= PasswordChangeForm(request.user, data=request.POST)
            if passwordForm.is_valid():
                passwordForm.save()
                messages.success(request, 'Password Updated Successfully')
                update_session_auth_hash(request,passwordForm.user)
                return redirect('user_profile')
        else:
            passwordForm= PasswordChangeForm(request.user)
        return render(request,'password_page.html', {'form': passwordForm, 'type':'Password Change'})
    else:
        return redirect('user_profile')

def changepassword2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            passwordForm = SetPasswordForm(user = request.user, data=request.POST)
            if passwordForm.is_valid():
                passwordForm.save()
                messages.success(request, 'password Set successfully')
                update_session_auth_hash(request,passwordForm.user)
                return redirect('user_profile')
        else:
            passwordForm = SetPasswordForm(user = request.user)
        return render(request,'password1_page.html', {'form':passwordForm,'type':'Set Password'})
    else:
        return redirect('user_profile')