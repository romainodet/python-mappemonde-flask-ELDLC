from model import Model
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Show artists
@app.route('/artists_simple.html')
def artists_simple():
    with Model() as model:
      artists=model.getArtistsSimple()
      return render_template('artists_simple.html', artists=artists)

@app.route('/artists.html')
def artists():
    with Model() as model:
      artists=model.getArtists()
      return render_template('artists.html', artists=artists)

# Show tracks
@app.route('/tracks_simple.html')
def tracks_simple():
    with Model() as model:
      tracks=model.getTracksSimple()
      return render_template('tracks_simple.html', tracks=tracks)

@app.route('/tracks.html')
def tracks():
    with Model() as model:
      tracks=model.getTracks()
      return render_template('tracks.html', tracks=tracks)


# Show albums
@app.route('/albums_simple.html')
def albums_simple():
    with Model() as model:
      albums=model.getAlbumsSimple()
      return render_template('albums_simple.html', albums=albums)

@app.route('/albums.html')
def albums():
    with Model() as model:
      albums=model.getAlbums()
      return render_template('albums.html', albums=albums)

# new routes should be defined here


# main application
if __name__ == '__main__':
    #under windows, there is a bug in a module which prevents the usage of debug=True
    #the bug should be fixed within days or weeks, but in the meantime do not enable debug
    app.run(host='0.0.0.0',debug=True)
