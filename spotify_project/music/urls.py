from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('search/', views.search, name='search'),  # Search page
    path('library/', views.library, name='library'),  # Your Library page
    path('song/<int:song_id>/play/', views.play_song, name='play_song'),
    path('song/<int:song_id>/like/', views.like_song, name='like_song'),

    # Registration section
    path('register/', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    