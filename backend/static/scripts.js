async function add_song() {
    const song_id = document.getElementById('song_id').value;
    const song_title = document.getElementById('song_title').value;
    const artist = document.getElementById('artist').value;
    const album = document.getElementById('album').value;
    const duration = document.getElementById('duration').value;

    const response = await fetch('/add_song', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ song_id, song_title, artist, album, duration})
    });

    const result = await response.json();
    alert(result.message);
    clearAddSongForm();
}

async function update_song() {
    const song_id = document.getElementById('update_song_id').value;
    const song_title = document.getElementById('update_song_title').value;
    const artist = document.getElementById('update_artist').value;
    const album = document.getElementById('update_album').value;
    const duration = document.getElementById('update_duration').value;

    const response = await fetch('/update_song', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ song_id, song_title, artist, album, duration })
    });

    const result = await response.json();
    alert(result.message);
    clearUpdateSongForm
}

async function add_playlist() {
    const playlist_id = document.getElementById('playlist_id').value;
    const playlist_title = document.getElementById('playlist_title').value;
    const description = document.getElementById('description').value

    const response = await fetch('/add_playlist', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({ playlist_id, playlist_title, description })
    });

    const result = await response.json();
    alert(result.message);
    clearAddPlaylistForm();
}

async function update_playlist() {
    const playlist_id = document.getElementById('update_playlist_id').value;
    const playlist_title = document.getElementById('update_playlist_title').value;
    const description = document.getElementById('update_description').value

    const response = await fetch('/update_playlist', {
        method: 'PUT',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({ playlist_id, playlist_title, description })
    });

    const result = await response.json();
    alert(result.message);
    clearUpdatePlaylistForm();
}

function getPlaylist() {
    const playlistId = document.getElementById('playlist_id').value;
    fetch(`/get_playlist/${playlistId}`)
        .then(response => response.json())
        .then(data => {
            const playlistDisplay = document.getElementById('playlist-display');
            playlistDisplay.innerHTML = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error fetching playlist:', error));
}

function clearForm(inputIds) {
    inputIds.forEach(id => {
        document.getElementById(id).value = '';
    });
}

function clearAddSongForm() {
    clearForm(['song_id', 'song_title', 'artist', 'album', 'duration']);
}

function clearUpdateSongForm() {
    clearForm(['update_song_id', 'update_song_title', 'update_artist', 'update_album', 'update_duration']);
}

function clearAddPlaylistForm() {
    clearForm(['playlist_id', 'playlist_title', 'description']);
}

function clearUpdatePlaylistForm() {
    clearForm(['update_playlist_id', 'update_playlist_title', 'update_description']);
}