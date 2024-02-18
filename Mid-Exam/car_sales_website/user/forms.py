from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
    firstName = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    lastName = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ['username','email']

class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email']