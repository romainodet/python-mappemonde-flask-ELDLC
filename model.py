import sqlite3

import sys

class Model:
    # Constructor, connect to database
    def __init__(self):
        self.con = sqlite3.connect('example.sqlite');
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    # Desctructor, disconnect from database
    def __exit__(self, type, value, traceback):
        if(self.con):
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
                            SELECT ar.Name as name, COUNT(al.ArtistId) as cpt_album
                            FROM Artist as ar, Album as al
                            WHERE ar.ArtistId = al.ArtistId
                            GROUP BY al.ArtistId
                            ORDER BY ar.Name ASC
                            """)

    # Display track information
    def getTracks(self):
        return self.sqlQuery("""
                            SELECT t.Name as track_name,al.Title as album_title,ar.Name as artist, ge.Name as genre
                            FROM
                            Track as t
                            LEFT JOIN Album as al ON t.AlbumId=al.AlbumId
                            LEFT JOIN Artist as ar ON al.ArtistId=ar.ArtistId
                            LEFT JOIN Genre as ge ON t.GenreId=ge.GenreId
                            ORDER BY al.Title ASC
                             """)

    # Display album information
    def getAlbums(self):
        return self.sqlQuery("""
                            SELECT al.AlbumId as num,al.Title as album_name,ar.Name as artist
                            FROM
                            Album as al
                            LEFT JOIN Artist as ar ON al.ArtistId=ar.ArtistId
                            ORDER BY ar.Name ASC
                             """)

    # Execute an SQL query and returns the result
    def sqlQuery(self,q):
        self.cur.execute(q)
        return self.cur.fetchall()
