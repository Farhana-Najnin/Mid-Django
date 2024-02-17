from django.urls import path
from . import views
urlpatterns = [
    # path('add/', views.music_album, name='album_page'),

    path('add/', views.MusicAlbum.as_view(), name='album'),
    path('adds/', views.Music_album, name='showing_album'),
    path('edit/<int:id>', views.EditAlbumView.as_view(), name='edit'),
    path('delete/<int:pk>', views.DeleteAlbumView.as_view(), name='delete'),
]
