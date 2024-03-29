from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Musician
from django import forms 

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'