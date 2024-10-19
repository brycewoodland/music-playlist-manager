from flask import Blueprint, request, jsonify
from flasgger import swag_from
from models.firestore_operations import ( 
    add_playlist,
    update_playlist, 
    get_playlist_with_songs, 
    get_all_playlists_with_songs, 
    delete_playlist, add_song_to_playlist, 
    delete_song_from_playlist
    )

playlist_bp = Blueprint('playlist_bp', __name__)

@playlist_bp.route('/playlist', methods=['POST'])
@swag_from({
    'summary': 'Add a new playlist',
    'description': 'Adds a new playlist to the database.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'playlist_id': {
                        'type': 'integer',
                        'example': 1
                    },
                    'playlist_title': {
                        'type': 'string',
                        'example': 'The Best of The Beatles'
                    },
                    'description': {
                        'type': 'string',
                        'example': 'My favorite songs by The Beatles'
                    }
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Playlist added successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Playlist added successfully!'
                    }
                }
            }
        }
    }
})
def add_playlist_route():
    data = request.json
    playlist_id = data['playlist_id']
    playlist_title = data['playlist_title']
    description = data['description']
    result = add_playlist(playlist_id, playlist_title, description)
    return jsonify(result)

@playlist_bp.route('/playlist/<int:playlist_id>', methods=['PUT'])
@swag_from({
    'summary': 'Update an existing playlist',
    'description': 'Updates the details of an existing playlist.',
    'parameters': [
        {
            'name': 'playlist_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the playlist to update',
            'example': 1
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'playlist_title': {
                        'type': 'string',
                        'example': 'Updated Playlist Title'
                    },
                    'description': {
                        'type': 'string',
                        'example': 'Updated description of the playlist'
                    }
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Playlist updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Playlist updated successfully!'
                    }
                }
            }
        },
        404: {
            'description': 'Playlist not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Playlist not found'
                    }
                }
            }
        }
    }
})
def update_playlist_route(playlist_id):
    data = request.json
    updates = {key: value for key, value in data.items() if key != 'playlist_id'}
    result = update_playlist(playlist_id, **updates)
    return jsonify(result)

@playlist_bp.route('/playlist', methods=['GET'])
@swag_from({
    'summary': 'Get all playlists',
    'description': 'Retrieves all playlists from the database along with their songs.',
    'responses': {
        200: {
            'description': 'All playlists retrieved successfully',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'playlist_id': {
                            'type': 'number',
                            'example': 1
                        },
                        'playlist_title': {
                            'type': 'string',
                            'example': 'The Best of The Beatles'
                        },
                        'description': {
                            'type': 'string',
                            'example': 'My favorite songs by The Beatles'
                        },
                        'songs': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'title': {
                                        'type': 'string',
                                        'example': 'Song Title'
                                    },
                                    'artist': {
                                        'type': 'string',
                                        'example': 'Artist Name'
                                    },
                                    'album': {
                                        'type': 'string',
                                        'example': 'Album Name'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
})
def get_all_playlists_route():
    result = get_all_playlists_with_songs()
    return jsonify(result)

@playlist_bp.route('/playlist/<int:playlist_id>', methods=['GET'])
@swag_from({
    'summary': 'Get a playlist by ID',
    'description': 'Retrieves a playlist by its ID along with its songs.',
    'parameters': [
        {
            'name': 'playlist_id',
            'in': 'path',
            'type': 'number',
            'required': True,
            'description': 'The ID of the playlist to retrieve',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Playlist retrieved successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'playlist_id': {
                        'type': 'number',
                        'example': 1
                    },
                    'playlist_title': {
                        'type': 'string',
                        'example': 'The Best of The Beatles'
                    },
                    'description': {
                        'type': 'string',
                        'example': 'My favorite songs by The Beatles'
                    },
                    'songs': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'title': {
                                    'type': 'string',
                                    'example': 'Song Title'
                                },
                                'artist': {
                                    'type': 'string',
                                    'example': 'Artist Name'
                                },
                                'album': {
                                    'type': 'string',
                                    'example': 'Album Name'
                                }
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Playlist not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Playlist not found.'
                    }
                }
            }
        }
    }
})
def get_playlist_route(playlist_id):
    result, status_code = get_playlist_with_songs(playlist_id)
    return jsonify(result), status_code

@playlist_bp.route('/playlist/<int:playlist_id>', methods=['DELETE'])
@swag_from({
    'summary': 'Delete a playlist by ID',
    'description': 'Deletes a playlist by its ID.',
    'parameters': [
        {
            'name': 'playlist_id',
            'in': 'path',
            'type': 'number',
            'required': True,
            'description': 'The ID of the playlist to delete',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Playlist deleted successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Playlist deleted successfully!'
                    }
                }
            }
        }
    }
})
def delete_playlist_route(playlist_id):
    result = delete_playlist(playlist_id)
    return jsonify(result)

@playlist_bp.route('/playlist/<int:playlist_id>/song/<int:song_id>', methods=['POST'])
@swag_from({
    'summary': 'Add a song to a playlist',
    'description': 'Adds a song to a specified playlist.',
    'parameters': [
        {
            'name': 'playlist_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the playlist',
            'example': 123
        },
        {
            'name': 'song_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the song to add',
            'example': 456
        }
    ],
    'responses': {
        200: {
            'description': 'Song added to playlist successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Song added to playlist successfully!'
                    }
                }
            }
        },
        404: {
            'description': 'Playlist or song not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Playlist or song not found'
                    }
                }
            }
        }
    }
})
def add_song_to_playlist_route(playlist_id, song_id):
    result, status_code = add_song_to_playlist(playlist_id, song_id)
    return jsonify(result), status_code

@playlist_bp.route('/playlist/<int:playlist_id>/song/<int:song_id>', methods=['DELETE'])
@swag_from({
    'summary': 'Delete a song from a playlist',
    'description': 'Deletes a song from a specified playlist.',
    'parameters': [
        {
            'name': 'playlist_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the playlist',
            'example': 123
        },
        {
            'name': 'song_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the song to delete',
            'example': 456
        }
    ],
    'responses': {
        200: {
            'description': 'Song deleted from playlist successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Song deleted from playlist successfully!'
                    }
                }
            }
        },
        404: {
            'description': 'Song not found in playlist',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Song not found in playlist'
                    }
                }
            }
        }
    }
})
def delete_song_from_playlist_route(playlist_id, song_id):
    result, status_code = delete_song_from_playlist(playlist_id, song_id)
    return jsonify(result), status_code