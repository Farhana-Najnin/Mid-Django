from django import forms 
from . models import album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = album
        fields = '__all__'