from flask import Blueprint, request, jsonify
from models.firestore_operations import add_song, update_song

song_bp = Blueprint('song_bp', __name__)

@song_bp.route('/add_song', methods=['POST'])
def add_song_route():
    data = request.json
    song_id = data['song_id']
    song_title = data['song_title']
    artist = data['artist']
    album = data['album']
    duration = data['duration']
    result = add_song(song_id, song_title, artist, album, duration)
    return jsonify(result)

@song_bp.route('/update_song', methods=['PUT'])
def update_song_route():
    data = request.json
    song_id = data['song_id']
    updates = {key: value for key, value in data.items() if key != 'song_id'}
    result = update_song(song_id, **updates)
    return jsonify(result)