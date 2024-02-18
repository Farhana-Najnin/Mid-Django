from django.urls import path
from . import views
urlpatterns = [
    path('adduser/', views.userSignUp, name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(),name='logout'),
    path('profile/', views.UserProfile,name = 'profile'),
    path('edit/', views.editProfile,name = 'edit')

]
