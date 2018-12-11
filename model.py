import os
import sqlite3


class Model:
    # Constructor, connect to database
    def __init__(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.con = sqlite3.connect('mapmonde.sqlite')
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    # Destructor, disconnect from database
    def __exit__(self, type, value, traceback):
        if (self.con):
            self.con.close()

    # Get the content of the Artist table
    def getInfoCountry(self):
        return self.sqlQuery("""
                            SELECT * FROM country
                            """)

    def getMonnaie(self, id):
        return self.sqlQuery("""
                           select country.id ,currency.Monnaie as `monnaie`, currency.CodeISO 
                           as `monnaie_iso` , currency.id  
                           from country, currency WHERE country.currency_id = currency.id AND country.id = '%s'
                            """ % (id))

    def getInfoOnlyCountry(self, id):
        return self.sqlQuery("""
                            select country.id , country.name as `pays`, country.motto 
      as `devise`,country.pib as `pib` from country WHERE country.id = '%s' 
    
                            """% (id))


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
