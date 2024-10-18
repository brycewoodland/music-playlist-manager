from flask import Blueprint, request, jsonify
from flasgger import swag_from
from models.firestore_operations import add_song, update_song, get_song, get_all_songs, delete_song

song_bp = Blueprint('song_bp', __name__)

@song_bp.route('/song', methods=['POST'])
@swag_from({
    'summary': 'Add a new song',
    'description': 'Adds a new song to the database.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'song_id': {
                        'type': 'string',
                        'example': '1'
                    },
                    'song_title': {
                        'type': 'string',
                        'example': 'Hey Jude'
                    },
                    'artist': {
                        'type': 'string',
                        'example': 'The Beatles'
                    },
                    'album': {
                        'type': 'string',
                        'example': 'The Beatles Again'
                    },
                    'duration': {
                        'type': 'string',
                        'example': '7:11'
                    }
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Song added successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Song added successfully!'
                    }
                }
            }
        }
    }
})
def add_song_route():
    data = request.json
    song_id = data['song_id']
    song_title = data['song_title']
    artist = data['artist']
    album = data['album']
    duration = data['duration']
    result = add_song(song_id, song_title, artist, album, duration)
    return jsonify(result)

@song_bp.route('/song', methods=['PUT'])
@swag_from({
    'summary': 'Update an existing song',
    'description': 'Updates the details of an existing song.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'song_id': {
                        'type': 'string',
                        'example': '1'
                    },
                    'song_title': {
                        'type': 'string',
                        'example': 'Hey Jude'
                    },
                    'artist': {
                        'type': 'string',
                        'example': 'The Beatles'
                    },
                    'album': {
                        'type': 'string',
                        'example': 'The Beatles Again'
                    },
                    'duration': {
                        'type': 'string',
                        'example': '7:11'
                    }
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Song updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Song updated successfully!'
                    }
                }
            }
        }
    }
})
def update_song_route():
    data = request.json
    song_id = data['song_id']
    updates = {key: value for key, value in data.items() if key != 'song_id'}
    result = update_song(song_id, **updates)
    return jsonify(result)

@song_bp.route('/song', methods=['GET'])
@swag_from({
    'summary': 'Get all songs',
    'description': 'Retrieves all songs from the database.',
    'responses': {
        200: {
            'description': 'All songs retrieved successfully',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'song_id': {
                            'type': 'string',
                            'example': '1'
                        },
                        'song_title': {
                            'type': 'string',
                            'example': 'Hey Jude'
                        },
                        'artist': {
                            'type': 'string',
                            'example': 'The Beatles'
                        },
                        'album': {
                            'type': 'string',
                            'example': 'The Beatles Again'
                        },
                        'duration': {
                            'type': 'string',
                            'example': '7:11'
                        }
                    }
                }
            }
        }
    }
})
def get_all_songs_route():
    result = get_all_songs()
    return jsonify(result)

@song_bp.route('/song/<string:song_id>', methods=['GET'])
@swag_from({
    'summary': 'Get a song by ID',
    'description': 'Retrieves a song by its ID.',
    'parameters': [
        {
            'name': 'song_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'The ID of the song to retrieve',
            'example': '1'
        }
    ],
    'responses': {
        200: {
            'description': 'Song retrieved successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'song_id': {
                        'type': 'string',
                        'example': '1'
                    },
                    'song_title': {
                        'type': 'string',
                        'example': 'Hey Jude'
                    },
                    'artist': {
                        'type': 'string',
                        'example': 'The Beatles'
                    },
                    'album': {
                        'type': 'string',
                        'example': 'The Beatles Again'
                    },
                    'duration': {
                        'type': 'string',
                        'example': '7:11'
                    }
                }
            }
        },
        404: {
            'description': 'Song not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Song not found.'
                    }
                }
            }
        }
    }
})
def get_song_route(song_id):
    result = get_song(song_id)
    return jsonify(result)

@song_bp.route('/song/<string:song_id>', methods=['DELETE'])
@swag_from({
    'summary': 'Delete a song by ID',
    'description': 'Deletes a song by its ID.',
    'parameters': [
        {
            'name': 'song_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'The ID of the song to delete',
            'example': '1'
        }
    ],
    'responses': {
        200: {
            'description': 'Song deleted successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Song deleted successfully!'
                    }
                }
            }
        }
    }
})
def delete_song_route(song_id):
    result = delete_song(song_id)
    return jsonify(result)