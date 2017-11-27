import os
import sqlite3


class Model:
    # Constructor, connect to database
    def __init__(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.con = sqlite3.connect('example.sqlite')
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    # Desctructor, disconnect from database
    def __exit__(self, type, value, traceback):
        if (self.con):
            self.con.close()

    # Get the content of the Artist table
    def getArtistsSimple(self):
        return self.sqlQuery("""
                            SELECT * FROM Artist
                            """)

    # Get the content of the Tracks table
    def getTracksSimple(self):
        return self.sqlQuery("""
                            SELECT * FROM Track
                             """)

    # Get the content of the Album table
    def getAlbumsSimple(self):
        return self.sqlQuery("""
                            SELECT * FROM Album
                             """)

    # Get the content of the Artsit Table and count number of album for each artist
    def getArtists(self):
        return self.sqlQuery("""
                            SELECT ar.Name AS name, COUNT(al.ArtistId) AS cpt_album
                            FROM Artist AS ar, Album AS al
                            WHERE ar.ArtistId = al.ArtistId
                            GROUP BY al.ArtistId
                            ORDER BY ar.Name ASC
                            """)

    # Display track information
    def getTracks(self):
        return self.sqlQuery("""
                            SELECT t.Name AS track_name,al.Title AS album_title,ar.Name AS artist, ge.Name AS genre
                            FROM
                            Track AS t
                            LEFT JOIN Album AS al ON t.AlbumId=al.AlbumId
                            LEFT JOIN Artist AS ar ON al.ArtistId=ar.ArtistId
                            LEFT JOIN Genre AS ge ON t.GenreId=ge.GenreId
                            ORDER BY al.Title ASC
                             """)

    # Display album information
    def getAlbums(self):
        return self.sqlQuery("""
                            SELECT al.AlbumId AS num,al.Title AS album_name,ar.Name AS artist
                            FROM
                            Album AS al
                            LEFT JOIN Artist AS ar ON al.ArtistId=ar.ArtistId
                            ORDER BY ar.Name ASC
                             """)

    # Execute an SQL query and returns the result
    def sqlQuery(self, q):
        res = self.cur.execute(q)
        return self.cur.fetchall()
