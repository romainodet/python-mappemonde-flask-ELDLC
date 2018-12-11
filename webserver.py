from model import Model
from flask import *

# Create flask application
app = Flask(__name__)


# Define all routes (URL)

@app.route('/')  # / is the URL
def index():
    # These log messages are just to show you how you can use them to debug your application
    app.logger.info('This is an information message')
    app.logger.warning('hum, something is not right')
    app.logger.error('Oops, that must be a bug')
    return render_template('index.html')


# Show artists (simple case)
@app.route('/info_country.html')
def info_country():
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        countrys = model.getInfoCountry()
        return render_template('info_country.html', countrys=countrys)

# Show single artist
@app.route('/onlyCountry/<id>')
def onlyCountry(id):
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        info = model.getInfoOnlyCountry(id)
        monnaie = model.getMonnaie(id)
        return render_template('country_one.html', info=info , monnaie=monnaie)



# Show artists (more complex case)
@app.route('/artists.html')
def artists():
    with Model() as model:
        artists = model.getArtists()
        return render_template('artists.html', artists=artists)


# Show tracks (simple case)
@app.route('/tracks_simple.html')
def tracks_simple():
    with Model() as model:
        tracks = model.getTracksSimple()
        return render_template('tracks_simple.html', tracks=tracks)


# Show tracks (more complex case)
@app.route('/tracks.html')
def tracks():
    with Model() as model:
        tracks = model.getTracks()
        return render_template('tracks.html', tracks=tracks)


# Show albums (simple case)
@app.route('/albums_simple.html')
def albums_simple():
    with Model() as model:
        albums = model.getAlbumsSimple()
        return render_template('albums_simple.html', albums=albums)


# Show albums (more complex case)
@app.route('/albums.html')
def albums():
    with Model() as model:
        albums = model.getAlbums()
        return render_template('albums.html', albums=albums)


# new routes should be defined here


# main application
if __name__ == '__main__':
    # under windows, there is a bug in a module which prevents the usage of debug=True
    # the bug should be fixed within days or weeks, but in the meantime do not enable debug
    app.run(host='127.0.0.1', debug=True)
