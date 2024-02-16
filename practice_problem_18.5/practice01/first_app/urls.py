from django.urls import path
from . import views
urlpatterns = [
    path('profile/',views.user_profile, name='user_profile'),
    path('signup/',views.user_signup, name='user_signup'),
    path('login/', views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),

    path('changepassword/', views.changepassword,name='changepassword'),

    path('changepassword2/',views.changepassword2,name='changepassword2'),
]