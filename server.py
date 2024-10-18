from flask import Flask
from flask_cors import CORS
from routes.song_routes import song_bp
from routes.playlist_routes import playlist_bp
from swagger import configure_swagger

from firebase_admin import firestore

db = firestore.client()

app = Flask(__name__)
CORS(app)

# Configure Swagger
configure_swagger(app)

# Register Blueprints
app.register_blueprint(song_bp)
app.register_blueprint(playlist_bp)

if __name__ == '__main__':
    app.run(debug=True)