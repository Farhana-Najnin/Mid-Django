from django.shortcuts import render
from store.models import Car
from category.models import Brand

def home(request, brand_slug = None):
    data = Car.objects.all()
    Car_category = Brand.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        data = Car.objects.filter(brand = brand)
    return render(request,'home.html',{'data': data, 'Car_category': Car_category})
