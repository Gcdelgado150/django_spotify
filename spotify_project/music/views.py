from rest_framework import viewsets
from .models import Artist, Album, Song, Playlist
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

def home(request):
    playlists = Playlist.objects.all()
    return render(request, 'index.html', {'playlists': playlists})

# Search view
def search(request):
    return render(request, 'search.html')

# Library view
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