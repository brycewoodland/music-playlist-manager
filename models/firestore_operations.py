import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('service-account-file.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_song(song_id, song_title, artist, album, duration):
    '''
    Adds a new song to the database.
    '''
    song_ref = db.collection('songs').document(str(song_id))  # Convert to string for Firestore
    song_ref.set({
        'song_id': song_id,
        'song_title': song_title,
        'artist': artist,
        'album': album,
        'duration': duration
    })
    return {'message': 'Song added successfully!'}

def update_song(song_id, **kwargs):
    '''
    Updates the details of a song.
    '''
    song_ref = db.collection('songs').document(str(song_id))  # Convert to string for Firestore
    if kwargs:
        song_ref.update(kwargs)
        return {'message': 'Song updated successfully.'}
    else:
        return {'message': 'No updates provided.'}

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
    song_ref = db.collection('songs').document(str(song_id))  # Convert to string for Firestore
    song = song_ref.get()
    if song.exists:
        return song.to_dict()
    else:
        return {'message': 'Song not found.'}

def delete_song(song_id):
    '''
    Deletes a song by its ID.
    '''
    song_ref = db.collection('songs').document(str(song_id))  # Convert to string for Firestore
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
    
def update_playlist(playlist_id, **kwargs):
    '''
    Updates the details of a playlist.
    '''
    playlist_ref = db.collection('playlists').document(str(playlist_id))
    if kwargs:
        playlist_ref.update(kwargs)
        return { 'message': 'Playlist updated successfully.'}
    else:
        return { 'message': 'No updates provided.'}
    
def get_all_playlists():
    '''
    Retrieves all playlists from the database.
    '''
    playlists_ref = db.collection('playlists')
    playlists = playlists_ref.stream()
    playlists_list = [playlist.to_dict() for playlist in playlists]
    
    if playlists_list:
        return playlists_list
    else:
        return { 'message': 'No playlists found.' }
    
def get_playlist(playlist_id):
    '''
    Retrieves a playlist by its ID.
    '''
    playlist_ref = db.collection('playlists').document(str(playlist_id)) 
    playlist = playlist_ref.get()
    if playlist.exists:
        return playlist.to_dict()
    else:
        return {'message': 'Playlist not found.'}

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
