from rest_framework import serializers
from .models import Artist, Album, Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)  # Nested serialization for read operations
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(), source='artist', write_only=True
    )  # Allow selecting artist by ID for write operations

    class Meta:
        model = Album
        fields = ['id', 'name', 'artist', 'artist_id', 'release_date']

class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)  # Nested serialization for read operations
    album_id = serializers.PrimaryKeyRelatedField(
        queryset=Album.objects.all(), source='album', write_only=True
    )  # Allow selecting album by ID for write operations

    class Meta:
        model = Song
        fields = ['id', 'name', 'album', 'album_id', 'file']
