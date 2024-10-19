import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('service-account-file.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_song(song_id, song_title, artist, album, duration):
    '''
    Adds a new song to the database.
    '''
    song_ref = db.collection('songs').document(str(song_id))  
    song_ref.set({
        'song_id': song_id,
        'song_title': song_title,
        'artist': artist,
        'album': album,
        'duration': duration
    })
    return {'message': 'Song added successfully!'}

def update_song(song_id, **updates):
    '''
    Updates an existing song by its ID.
    '''
    try:
        song_ref = db.collection('songs').document(str(song_id))
        if not song_ref.get().exists:
            return {'message': 'Song not found'}, 404
        
        song_ref.update(updates)
        return {'message': 'Song updated successfully!'}, 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'message': f'An error occurred while updating the song: {str(e)}'}, 500

def get_all_songs():
    '''
    Retrieves all songs from the database.
    '''
    songs_ref = db.collection('songs')
    songs = songs_ref.stream()
    songs_list = [song.to_dict() for song in songs]
    
    if songs_list:
        return songs_list
    else:
        return {'message': 'No songs found.'}

def get_song(song_id):
    '''
    Retrieves a song by its ID.
    '''
    song_ref = db.collection('songs').document(str(song_id))  
    song = song_ref.get()
    if song.exists:
        return song.to_dict()
    else:
        return {'message': 'Song not found.'}

def delete_song(song_id):
    '''
    Deletes a song by its ID.
    '''
    song_ref = db.collection('songs').document(str(song_id))  
    song_ref.delete()
    return {'message': 'Song deleted successfully!'}

def update_user(user_id, **kwargs):
    '''
    Updates user information.
    '''
    user_ref = db.collection('users').document(str(user_id))
    if kwargs:
        user_ref.update(kwargs)
        return {'message': 'User updated successfully.'}
    else:
        return {'message': 'No updates provided.'}
    
def update_playlist(playlist_id, **updates):
    '''
    Updates an existing playlist by its ID.
    '''
    try:
        playlist_ref = db.collection('playlists').document(str(playlist_id))
        if not playlist_ref.get().exists:
            return {'message': 'Playlist not found'}, 404
        
        playlist_ref.update(updates)
        return {'message': 'Playlist updated successfully!'}, 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'message': f'An error occurred while updating the playlist: {str(e)}'}, 500
    
def get_all_playlists_with_songs():
    '''
    Retrieves all playlists along with their songs.
    '''
    playlists_ref = db.collection('playlists')
    playlists = playlists_ref.stream()
    
    all_playlists = []
    for playlist in playlists:
        playlist_data = playlist.to_dict()
        playlist_id = playlist.id
        
        playlist_entries_ref = db.collection('playlist_entries').where('playlist_id', '==', playlist_id)
        playlist_entries = playlist_entries_ref.stream()
        
        songs = []
        for entry in playlist_entries:
            song_id = entry.to_dict()['song_id']
            song_ref = db.collection('songs').document(song_id)
            song = song_ref.get().to_dict()
            if song:
                songs.append(song)
        
        playlist_data['songs'] = songs
        all_playlists.append(playlist_data)
    
    return all_playlists
    
def get_playlist_with_songs(playlist_id):
    '''
    Retrieves a playlist by its ID along with its songs.
    '''
    try:
        # Retrieve the playlist document
        playlist_ref = db.collection('playlists').document(str(playlist_id))
        playlist_snapshot = playlist_ref.get()
        
        if not playlist_snapshot.exists:
            return {'message': 'Playlist not found'}, 404
        
        playlist = playlist_snapshot.to_dict()
        
        # Retrieve the playlist entries
        playlist_entries_ref = db.collection('playlist_entries').where('playlist_id', '==', str(playlist_id))
        playlist_entries = playlist_entries_ref.stream()
        
        songs = []
        for entry in playlist_entries:
            entry_data = entry.to_dict()
            song_id = entry_data.get('song_id')
            if not song_id:
                continue
            
            # Retrieve the song document
            song_ref = db.collection('songs').document(song_id)
            song_snapshot = song_ref.get()
            
            if song_snapshot.exists:
                song = song_snapshot.to_dict()
                songs.append(song)
            else:
                print(f"Song with ID {song_id} not found.")
        
        playlist['songs'] = songs
        return playlist, 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'message': 'An error occurred while retrieving the playlist'}, 500

def delete_playlist(playlist_id):
    '''
    Deletes a playlist by its ID.
    '''
    playlist_ref = db.collection('playlists').document(str(playlist_id))
    playlist_ref.delete()
    return {'message': 'Playlist deleted successfully!'}

def add_playlist(playlist_id, playlist_title, description):
    '''
    Adds a new playlist to the database.
    '''
    playlist_ref = db.collection('playlists').document(str(playlist_id))
    playlist_ref.set({
        'playlist_id': playlist_id,
        'playlist_title': playlist_title,
        'description': description
    })
    return {'message': 'Playlist added successfully!'}

def add_song_to_playlist(playlist_id, song_id):
    '''
    Adds a song to a playlist by its ID.
    '''
    try:
        # Check if the playlist exists
        playlist_ref = db.collection('playlists').document(str(playlist_id))
        if not playlist_ref.get().exists:
            return {'message': 'Playlist not found'}, 404
        
        # Check if the song exists
        song_ref = db.collection('songs').document(str(song_id))
        if not song_ref.get().exists:
            return {'message': 'Song not found'}, 404
        
        # Add the song to the playlist using Firestore's automatic ID generation
        playlist_entry_ref = db.collection('playlist_entries').document()
        playlist_entry_ref.set({
            'playlist_id': str(playlist_id),
            'song_id': str(song_id)
        })
        return {'message': 'Song added to playlist successfully!'}, 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'message': f'An error occurred while adding the song to the playlist: {str(e)}'}, 500

def get_songs_in_playlist(playlist_id):
    '''
    Retrieves all songs in a playlist by its ID.
    '''
    playlist_entries_ref = db.collection('playlist_entries').where('playlist_id', '==', playlist_id)
    playlist_entries = playlist_entries_ref.stream()
    
    songs = []
    for entry in playlist_entries:
        song_id = entry.to_dict()['song_id']
        song_ref = db.collection('songs').document(song_id)
        song = song_ref.get().to_dict()
        if song:
            songs.append(song)
    
    if not songs:
        return {'message': 'Playlist not found or no songs in playlist'}, 404
    
    return {'songs': songs}

def delete_song_from_playlist(playlist_id, song_id):
    '''
    Deletes a song from a playlist by its ID.
    '''
    playlist_entries_ref = db.collection('playlist_entries').where('playlist_id', '==', playlist_id).where('song_id', '==', song_id)
    playlist_entries = playlist_entries_ref.stream()
    
    deleted = False
    for entry in playlist_entries:
        entry.reference.delete()
        deleted = True
    
    if not deleted:
        return {'message': 'Song not found in playlist'}, 404
    
    return {'message': 'Song deleted from playlist successfully!'}