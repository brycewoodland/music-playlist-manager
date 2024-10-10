import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('service-account-file.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_user(user_id, first_name, last_name):
    """
    Adds a new user to a collection in firebase
    """
    user_data = {
        'first_name': first_name,
        'last_name': last_name
    }
    db.collection('users').document(user_id).set(user_data)
    return {'message': 'User added succesfully!'}

def add_song(song_id, song_title, artist, album, duration):
    '''
    Adds a song to the database.
    '''
    song_data = {
        'song_id': song_id,
        'song_title': song_title,
        'artist': artist,
        'album': album,
        'duration': duration
    }
    db.collection('songs').document(song_id).set(song_data)
    return {'message': 'Song added successfully'}

def add_playlist(playlist_id, user_id, playlist_title, description):
    '''
    Adds a playlist to the database.
    '''
    playlist_ref = db.collection('playlists').document(playlist_id)
    playlist_ref.set({
        'user_id': user_id,
        'playlist_title': playlist_title,
        'description': description,
        'date': firestore.SERVER_TIMESTAMP
    })
    return {'message': 'Playlist added succesfully!'}

def add_song_to_playlist(playlist_id, song_id):
    '''
    Adds a song to the playlist.
    '''
    playlist_entry_ref = db.collection('playlist_entries').document()
    playlist_entry_ref.set({
        'playlist_id': playlist_id,
        'song_id': song_id
    })
    return {'message': 'Song add to the playlist succesfully!'}

def update_song(song_id, **kwargs):
    '''
    Updates the details of a song
    '''
    song_ref = db.collection('songs').document(song_id)
    if kwargs:
        song_ref.update(kwargs)
        return {'message': 'Song updated successfully!'}
    else:
        return {'message': 'No updates provided.'}

def update_user(user_id, **kwargs):
    '''
    Updates user information.
    '''
    user_ref = db.collection('users').document(user_id)
    if kwargs:
        user_ref.update(kwargs)
        return {'message': 'User updated successfully.'}
    else:
        return {'message': 'No updates provided.'}