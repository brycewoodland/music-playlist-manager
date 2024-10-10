from flask import Flask, render_template
from routes.song_routes import song_bp
from routes.playlist_routes import playlist_bp

app = Flask(__name__)

app.register_blueprint(song_bp)
app.register_blueprint(playlist_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)