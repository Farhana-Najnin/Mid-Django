from django.urls import path 
from . import views

urlpatterns = [
    path('car/', views.carPost.as_view(), name='cars_post_page'),

    path('details/<int:id>', views.CarDetail.as_view(), name='car_detail'),

    path('history/', views.view_order_history, name= 'order_history'),

    path('carbuy/<int:id>/', views.buy_car, name = 'buy_car')
]
