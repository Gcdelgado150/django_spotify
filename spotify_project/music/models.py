from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()

    def __str__(self):
        return f'{self.name}'


class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')  # Add this line
    file = models.FileField(upload_to='songs/')

    def __str__(self):
        return f'{self.name}'

# Playlist Model
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
    
class User(models.Model):
    # Add liked songs Many-to-Many field
    liked_songs = models.ManyToManyField(Song, related_name='liked_by', blank=True)
