from django.urls import path 
from .import views
urlpatterns = [
    # path('add/',views.musician, name='musician_page'),
    # path('register/',views.registration, name='registration_page'),
    # path('login/',views.log_in, name='login_page'),
    path('add/',views.AddMusicianView.as_view(), name='musician'),
    path('register/',views.UserSignupView.as_view(), name='signup'),
    path('login/',views.UserLoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
]
