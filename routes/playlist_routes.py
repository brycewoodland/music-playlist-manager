from flask import Blueprint, request, jsonify
from flasgger import swag_from
from models.firestore_operations import add_playlist, update_playlist, get_playlist, get_all_playlists, delete_playlist

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

@playlist_bp.route('/playlist', methods=['PUT'])
@swag_from({
    'summary': 'Update an existing playlist',
    'description': 'Updates the details of an existing playlist.',
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
        }
    }
})
def update_playlist_route():
    data = request.json
    playlist_id = data['playlist_id']
    updates = {key: value for key, value in data.items() if key != 'playlist_id'}
    result = update_playlist(playlist_id, **updates)
    return jsonify(result)

@playlist_bp.route('/playlist', methods=['GET'])
@swag_from({
    'summary': 'Get all playlists',
    'description': 'Retrieves all playlists from the database.',
    'responses': {
        200: {
            'description': 'All playlists retrieved successfully',
            'schema': {
                'type': 'array',
                'items': {
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
        }
    }
})
def get_all_playlists_route():
    result = get_all_playlists()
    return jsonify(result)

@playlist_bp.route('/playlist/<int:playlist_id>', methods=['GET'])
@swag_from({
    'summary': 'Get a playlist by ID',
    'description': 'Retrieves a playlist by its ID.',
    'parameters': [
        {
            'name': 'playlist_id',
            'in': 'path',
            'type': 'integer',
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
    result = get_playlist(playlist_id)
    return jsonify(result)

@playlist_bp.route('/playlist/<int:playlist_id>', methods=['DELETE'])
@swag_from({
    'summary': 'Delete a playlist by ID',
    'description': 'Deletes a playlist by its ID.',
    'parameters': [
        {
            'name': 'playlist_id',
            'in': 'path',
            'type': 'integer',
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