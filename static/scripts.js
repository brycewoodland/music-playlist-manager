async function addSong() {
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

async function updateSong() {
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
}

function clearAddSongForm() {
    document.getElementById('song_id').value = '';
    document.getElementById('song_title').value = '';
    document.getElementById('artist').value = '';
    document.getElementById('album').value = '';
    document.getElementById('duration').value = '';
}

function clearUpdateSongForm() {
    document.getElementById('update_song_id').value = '';
    document.getElementById('update_song_title').value = '';
    document.getElementById('update_artist').value = '';
    document.getElementById('update_album').value = '';
    document.getElementById('update_duration').value = '';
}