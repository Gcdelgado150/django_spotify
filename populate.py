from spotify_project.music.models import Artist, Album, Song, Playlist

# Create sample artists
artist1 = Artist.objects.create(name="Artist 1", bio="Artist 1 bio")
artist2 = Artist.objects.create(name="Artist 2", bio="Artist 2 bio")

# Create albums
album1 = Album.objects.create(title="Album 1", artist=artist1, release_date="2023-01-01")
album2 = Album.objects.create(title="Album 2", artist=artist2, release_date="2023-05-15")

# Create songs
song1 = Song.objects.create(title="Song 1", artist=artist1, album=album1, duration=180, audio_file="path_to_audio_file")
song2 = Song.objects.create(title="Song 2", artist=artist1, album=album1, duration=200, audio_file="path_to_audio_file")
song3 = Song.objects.create(title="Song 3", artist=artist2, album=album2, duration=210, audio_file="path_to_audio_file")

# Create a playlist and add songs to it
playlist = Playlist.objects.create(name="My Playlist", description="A cool playlist")
playlist.songs.add(song1, song2)

# Verify if the data is added
print("Artists:", Artist.objects.all())
print("Albums:", Album.objects.all())
print("Songs:", Song.objects.all())
print("Playlists:", Playlist.objects.all())
