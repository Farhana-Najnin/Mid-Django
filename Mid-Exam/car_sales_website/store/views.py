from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView
from . import models 
from . import forms  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
# Create your views here.

class carPost(CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'home.html'
    success_url = reverse_lazy('post.html')
    def form_valid(self, form):
        return super().form_valid(form)

class CarDetail(DetailView):
    model = models.Car
    template_name = 'details.html'
    pk_url_kwarg = 'id'

    def post(self, *args, **kwargs):
            comment_form = forms.CommentForm(data=self.request.POST)
            post = self.get_object()
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post 
                new_comment.save()
            return self.get(self, *args, **kwargs)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context 
    
@login_required
def buy_car(request,id):
    car = get_object_or_404(models.Car, pk=id)
    if request.method == 'POST':
        if car.quantity > 0:
            order = models.Order(user=request.user, car=car)
            order.save()
            car.quantity -= 1
            car.save()
            messages.success(request, 'You buy car Successfully')
            return redirect('order_history')
        else:
            return render(request, 'stock.html', 
            {'car': car})
    return render(request,'carBuy.html',{'car':car})

@login_required
def view_order_history(request):
    user = get_user(request)
    order = models.Order.objects.filter(user=user)
    return render(request, 'profile.html', {'orders': order})
