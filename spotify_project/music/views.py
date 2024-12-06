from rest_framework import viewsets
from .models import Artist, Album, Song, Playlist
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

@login_required
def home(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'index.html', {'playlists': playlists})

# Search view
@login_required
def search(request):
    query = request.GET.get('query', '')  # Get the search query from the form
    songs = Song.objects.filter(name__icontains=query) if query else Song.objects.all()
    return render(request, 'search.html', {'songs': songs, 'query': query})

# Library view
@login_required
def library(request):
    return render(request, 'library.html')

def play_song(request, song_id):
    # Get the song by ID
    song = Song.objects.get(id=song_id)
    
    # Ensure the file URL is correct
    file_url = song.file.url  # This gives the relative URL like /media/songs/song_name.mp3
    full_file_url = settings.MEDIA_URL + file_url.lstrip(settings.MEDIA_URL)  # Get the full URL

    # Return song data
    response_data = {
        'name': song.name,
        'artist': song.artist.name,
        'file_url': full_file_url  # Send the full URL
    }
    return JsonResponse(response_data)

def like_song(request, song_id):
    if request.user.is_authenticated:
        song = Song.objects.get(id=song_id)
        user = request.user

        # Assuming you have a Many-to-Many field `liked_songs` on the user model
        user.liked_songs.add(song)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'User not authenticated'})
    
"""
Login section
"""
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
