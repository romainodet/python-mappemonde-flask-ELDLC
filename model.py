import os
import sqlite3


class Model:
    # Constructor, connect to database
    def __init__(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.con = sqlite3.connect('mapmonde')
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    # Destructor, disconnect from database
    def __exit__(self, type, value, traceback):
        if (self.con):
            self.con.close()

    # Get the content of the Artist table
    def getArtistsSimple(self):
        return self.sqlQuery("""
                            SELECT * FROM country
                            """)

    def getArtist(self, id):
        return self.sqlQuery("""
                            SELECT * FROM country
                            """ % (id))

    def getAlbumsOfArtist(self, id):
        return self.sqlQuery("""
          SELECT * FROM country
        """ % (id))


    # Get the content of the Tracks table
    def getTracksSimple(self):
        return self.sqlQuery("""
                            SELECT * FROM country
                             """)

    # Get the content of the Album table
    def getAlbumsSimple(self):
        return self.sqlQuery("""
                            SELECT * FROM country
                             """)

    # Get the content of the Artsit Table and count number of album for each artist
    def getArtists(self):
        return self.sqlQuery("""
                           
                            """)

    # Display track information
    def getTracks(self):
        return self.sqlQuery("""
                           
                             """)

    # Display album information
    def getAlbums(self):
        return self.sqlQuery("""
                           
                             """)

    # Execute an SQL query and returns the result
    def sqlQuery(self, q):
        res = self.cur.execute(q)
        return self.cur.fetchall()
