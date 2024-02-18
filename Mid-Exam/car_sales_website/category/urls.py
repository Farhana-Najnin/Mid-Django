from django.urls import path 
from . import views 

urlpatterns = [
    path('Categories/',views.categoryView.as_view(),name='category_view')
]


 