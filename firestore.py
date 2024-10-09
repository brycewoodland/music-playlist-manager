import firebase_admin
from firebase_admin import credentials, firestore

# Application Default Credentials 
cred = credentials.Certificate('service-account-file.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def add_user(user_id, first_name, last_name):
    """
    Adds a new user to a collection in firebase
    """
    user_ref = db.collection('users').document(user_id)
    user_ref.set({
        'first_name': first_name,
        'last_name': last_name
    })
    print('User added successfully!')

def add_song(song_id, song_title, artist, album, duration):
    '''
    Adds a song to the database.
    '''
    song_ref = db.collection('songs').document(song_id)
    song_ref.set({
        'title': song_title,
        'artist': artist,
        'album': album,
        'duration': duration
    })
    print('Song added successfully')

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
    print('Playlist added succesfully!')

def add_song_to_playlist(playlist_id, song_id):
    '''
    Adds a song to the playlist.
    '''
    playlist_entry_ref = db.collection('playlist_entries').document()
    playlist_entry_ref.set({
        'playlist_id': playlist_id,
        'song_id': song_id
    })
    print('Song add to the playlist succesfully!')

def update_song(song_id, **kwargs):
    '''
    Updates the details of a song
    '''
    song_ref = db.collection('songs').document(song_id)
    if kwargs:
        song_ref.update(kwargs)
        print('Song updated successfully!')
    else:
        print('No updates provided.')


add_user('1', 'Bryce', 'Woodland')
add_song('1', 'Come Together', 'The Beatles', 'Abbey Road', 259)
add_song('2', 'Here Comes the Sun', 'The Beatles', 'Abbey Road', 259)
add_playlist('1', '1', 'Best of The Beatles', 'Songs that I like by The Beatles')
add_song_to_playlist('1', '1')
add_song_to_playlist('1', '2')

update_song('2', duration=185)