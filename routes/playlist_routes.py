from flask import Blueprint, request, jsonify
from models.firestore_operations import add_playlist, add_song_to_playlist

playlist_bp = Blueprint('playlist_bp', __name__)

@playlist_bp.route('/add_playlist', methods=['POST'])
def add_playlist_route():
    data = request.json
    playlist_id = data['playlist_id']
    user_id = data['user_id']
    playlist_title = data['playlist_title']
    description = data['description']
    result = add_playlist(playlist_id, user_id, playlist_title, description)
    return jsonify(result)

@playlist_bp.route('/add_song_to_playlist', methods=['POST'])
def add_song_to_playlist_route():
    data = request.json
    playlist_id = data['playlist_id']
    song_id = data['song_id']
    result = add_song_to_playlist(playlist_id, song_id)
    return jsonify(result)