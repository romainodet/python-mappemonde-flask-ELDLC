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
                            select country.iso, country.id , country.name as `pays`, country.motto 
      as `devise`,country.pib as `pib` from country WHERE country.id = '%s' 
    
                            """% (id))

    def getCompanies(self):
        return self.sqlQuery("""
        
        select country.iso as 'iso',company.name as `company`, company.turnover as `CA`, country.name as `pays`, activity.activity_name as `domaine`
        from company, country, company_country, activity
        where company.activity_id = activity.id and country.id = company_country.country_id and company.id = company_country.company_id
        order by country.name asc
        """)

    def getCancer(self):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`, cancer.value as `nbr_cancer`, cancer.year as `stat_year`
from country, cancer where country.id = cancer.country_id order by nbr_cancer desc

                """)

    def getAlcohol(self):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`,
alcohol.amount as `alc`, alcohol.date as `stat_year`
from country, alcohol where country.id = alcohol.country_id order by pays asc
""")

    def getKidnap(self):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`,
kidnap.Amount as `kidnap`, kidnap.Date as `stat_year`
from country, kidnap where country.id = kidnap.Country order by kidnap desc
""")

    def getCinema(self):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`,
price_cinema.Amount as `cinema`, price_cinema.Date as `stat_year`
from country, price_cinema where country.id = price_cinema.country_id order by pays asc
        """)
    # Execute an SQL query and returns the result
    def sqlQuery(self, q):
        res = self.cur.execute(q)
        return self.cur.fetchall()
