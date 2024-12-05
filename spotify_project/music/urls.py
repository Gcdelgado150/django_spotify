from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# URL patterns for the music app
urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('search/', views.search, name='search'),  # Search page
    path('library/', views.library, name='library'),  # Your Library page
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
