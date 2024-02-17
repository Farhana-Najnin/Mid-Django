from typing import Any
from django.shortcuts import render
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
# from django.shortcuts import render,redirect
from .import forms 
from . import models
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from Album.models import album
# Create your views here.

def Music_album(request):
    data = album.objects.all()
    return render(request, 'show_album.html', {'data':data})

# class Musics_album(ListView):
#     model = album
#     template_name = 'show_album.html'
#     context_object_name = 'data'
# class based view
@method_decorator(login_required, name = 'dispatch')
class MusicAlbum(CreateView):
    model = models.album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('album')

    def form_valid(self, form):
        messages.success(self.request, 'Adding Album Successfully!')
        return super().form_valid(form)

# class based view 
@method_decorator(login_required, name = 'dispatch')
class EditAlbumView(UpdateView):
    model = models.album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('home_page')

    def get_object(self):
        id = self.kwargs.get('id')
        return models.album.objects.get(pk=id)

    def form_valid(self, form):
        return super().form_valid(form)
    
#class based View
@method_decorator(login_required, name = 'dispatch')
class DeleteAlbumView(DeleteView):
    model = models.album
    success_url = reverse_lazy('album')
    template_name = 'delete.html'

