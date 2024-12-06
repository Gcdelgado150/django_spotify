
let isPlaying = false;

// Get references to DOM elements
const currentTimeSpan = document.getElementById('current-time');
const durationSpan = document.getElementById('duration');
const songTitle = document.getElementById('song-title');
const artistName = document.getElementById('artist-name');
const albumArt = document.getElementById('album-art');

// Example playlist
const playlist = [
  {
    title: "Sample Song 1",
    artist: "Artist 1",
    albumArt: "/static/images/sample1.jpg",
    src: "/static/songs/sample1.mp3"
  },
  {
    title: "Sample Song 2",
    artist: "Artist 2",
    albumArt: "/static/images/sample2.jpg",
    src: "/static/songs/sample2.mp3"
  }
];

let currentSongIndex = 0;

// Load the firss bar and current time


// Format time in MM:SS format
function formatTime(seconds) {
  const mins = Math.floor(seconds / 60);
  const secs = Math.floor(seconds % 60);
  return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
}

document.addEventListener('DOMContentLoaded', function() {
  const playButtons = document.querySelectorAll('.play-song');

  playButtons.forEach(button => {
      button.addEventListener('click', function() {
          const songId = this.getAttribute('data-song-id');
          
          fetch(`/song/${songId}/play/`)
              .then(response => response.json())
              .then(data => {
                // Update the footer (now playing) text with the song details
                const nowPlayingSpan = document.querySelector('.now-playing span');
                nowPlayingSpan.textContent = `${data.name} - ${data.artist}`;

                  // const albumCover = document.getElementById('albumCover');
                  // albumCover.src = data.album.name;  // Assume this field is in your response
                  
                  // Update the audio player source
                  const audioPlayer = document.getElementById('audioPlayer');
                  audioPlayer.src = data.file_url;

                  // Load the new song and play it
                  audioPlayer.load();
                  audioPlayer.play();
              })
              .catch(error => {
                  console.error('Error:', error);
              });
      });
  });

  // Handle Like Buttons
  const likeButtons = document.querySelectorAll('.like-song');
    
  likeButtons.forEach(button => {
      button.addEventListener('click', function() {
          const songId = this.getAttribute('data-song-id');
          
          // Fetch request to like the song
          fetch(`/song/${songId}/like/`, { method: 'POST' })
              .then(response => response.json())
              .then(data => {
                  if (data.success) {
                      alert('Song added to your liked songs!');
                  } else {
                      alert('Error liking song!');
                  }
              })
              .catch(error => console.error('Error liking song:', error));
      });
  });
  
});