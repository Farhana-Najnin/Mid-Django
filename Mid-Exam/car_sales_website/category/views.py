from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View
from .import models 
from .import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
@method_decorator(login_required, name='dispatch')
class categoryView(View):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'home.html'
    success_url = reverse_lazy('category_wise_car')
    
    def form_valid(self, form):
        return super().form_valid(form)
    