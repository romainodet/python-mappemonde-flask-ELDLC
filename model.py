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

    # obtenir toute la table pays
    def getInfoCountry(self):
        return self.sqlQuery("""
                            SELECT * FROM country
                            """)

    # obtenir l'id pays, le nom de la monnaie, le code iso de la monnaie. jointure entre currency et country
    def getMonnaie(self, id):
        return self.sqlQuery("""
                           select country.id ,currency.Monnaie as `monnaie`, currency.CodeISO 
                           as `monnaie_iso` , currency.id  
                           from country, currency WHERE country.currency_id = currency.id AND country.id = '%s'
                            """ % (id))

    # obtenir des infos pour un seul pays : Numéro iso pays, id du pays dans la bdd, nom du pays, sa devise, son PIB. condition : verif id

    def getInfoOnlyCountry(self, id):
        return self.sqlQuery("""
                            select country.iso, country.id , country.name as `pays`, country.motto 
      as `devise`,country.pib as `pib` from country WHERE country.id = '%s' 
    
                            """ % (id))

    # obtenir des infos sur les entreprises (n-n) : ISO du pays, nom entreprise, CA entreprise, nom du pays, domaine d'activité de l'entrprise.
    # jointure nn entre company et country (car une entrprise peut etre localisé dans différents pays), cela grace à comany_country
    def getCompanies(self):
        return self.sqlQuery("""
        
        select country.iso as 'iso',company.name as `company`, company.turnover as `CA`, country.name as `pays`, activity.activity_name as `domaine`
        from company, country, company_country, activity
        where company.activity_id = activity.id and country.id = company_country.country_id and company.id = company_country.company_id
        order by country.name asc
        """)

    # obtenir l'iso pays, le nombre de cancer, l'année de la stat, et le nom du pays
    # jointure : id pays dans country et id pays dans cancer
    def getCancer(self):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`, cancer.value as `nbr_cancer`, cancer.year as `stat_year`
from country, cancer where country.id = cancer.country_id order by nbr_cancer desc

                """)

    # obtenir le nombre de litre d'alcool : iso pays, nom pays, valeur, date de la stat
    # jointure : id pays dans country et id pays dans alcool
    def getAlcohol(self):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`,
alcohol.amount as `alc`, alcohol.date as `stat_year`
from country, alcohol where country.id = alcohol.country_id order by pays asc
""")

    # obtenir le nombre de kidnapping : iso pays, nom pays, valeur kidnap, date de la stat
    # jointure : id pays dans country et id pays dans kidnap
    def getKidnap(self):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`,
kidnap.Amount as `kidnap`, kidnap.Date as `stat_year`
from country, kidnap where country.id = kidnap.Country order by kidnap desc
""")

    # obtenir le prix d'une place de cinéma : iso pays; prix de la place, nom du pays, date de la stat
    def getCinema(self):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`,
price_cinema.Amount as `cinema`, price_cinema.Date as `stat_year`
from country, price_cinema where country.id = price_cinema.country_id order by pays asc
        """)

    # pour la page d'accueil

    # obtenir pour la page d'accueil (liste pays), l'id du pays et le nom du pays et organiser par ordre asc
    def getCountryNew(self):
        return self.sqlQuery("""
        select country.name as `name`, country.id as 'id' from country ORDER BY name asc
        """)

    # TOUTES LES REQUETES A PARTIR D'ICI SONT POUR LA CARTE ET LA LISTE DEROULANTE CAR CHAQUE PAYS EST INDIVIDUALISE

    # obrenir les informations pour un seul pays, condition id

    def getInfoOnlyCountryNew(self, id):
        return self.sqlQuery("""
        select country.iso, country.id , country.name as `pays`, country.motto
      as `devise`,country.pib as `pib` from country WHERE country.id = '%s'
      """ % (id))

    # obtenir les infos sur la monnaie condtion id
    # jointure id pays dans currency et id pays dans country
    def getMonnaieNew(self, id):
        return self.sqlQuery(""" 
        select country.id ,currency.Monnaie as `monnaie`, currency.CodeISO
                           as `monnaie_iso` , currency.id
                           from country, currency WHERE country.currency_id = currency.id AND country.id = '%s'
                           """ % (id))

    # obtenir les infos sur les entreprises du pays condtion id
    # jointure : comme au dessus n-n : activity-country-company
    def getCompanyNew(self, id):
        return self.sqlQuery("""
        select country.iso as 'iso',company.name as `company`, company.turnover as `CA`, country.name as `pays`, activity.activity_name as `domaine`
        from company, country, company_country, activity
        where company.activity_id = activity.id and country.id = company_country.country_id and company.id = company_country.company_id
        and country.id = '%s'
        """ % (id))

    # nombre de cancer pour le pays condtion id
    # jointure entre id country et id country dans cancer
    def getCancerNew(self, id):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`, cancer.value as `nbr_cancer`, cancer.year as `stat_year`
from country, cancer where country.id = cancer.country_id and country.id = '%s'
""" % (id))

    # obtenir le nombre de litre bu condtion id
    #  jointure entre id country et id country dans alcool
    def getAlcoholNew(self, id):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`,
alcohol.amount as `alc`, alcohol.date as `stat_year`
from country, alcohol where country.id = alcohol.country_id and country.id = '%s'
""" % (id))

    # obtenir le nombre de kidnapping condtion id
    def getKidnapNew(self, id):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`,
kidnap.Amount as `kidnap`, kidnap.Date as `stat_year`
from country, kidnap where country.id = kidnap.Country and country.id = '%s'
""" % (id))

    # obtenir le prix d'une place de ciné condtion id
    def getCinemaNew(self, id):
        return self.sqlQuery("""
        select country.iso as 'iso',country.name as `pays`,
price_cinema.Amount as `cinema`, price_cinema.Date as `stat_year`
from country, price_cinema where country.id = price_cinema.country_id and country.id = '%s'
""" % (id))

    # FOR THE MAP
    # same but change condtion id by condition iso because card works only with iso code
    def getInfoOnlyCountryNew_map(self, id):
        return self.sqlQueryS("""
        select country.iso, country.id , country.name as `pays`, country.motto
      as `devise`,country.pib as `pib` from country WHERE country.iso = '%s'
      """ % (id))

    def getMonnaieNew_map(self, id):
        return self.sqlQueryS(""" 
        select country.id ,currency.Monnaie as `monnaie`, currency.CodeISO
                           as `monnaie_iso` , currency.id
                           from country, currency WHERE country.currency_id = currency.id AND country.iso = '%s'
                           """ % (id))

    def getCompanyNew_map(self, id):
        return self.sqlQueryS("""
        select country.iso as 'iso',company.name as `company`, company.turnover as `CA`, country.name as `pays`, activity.activity_name as `domaine`
        from company, country, company_country, activity
        where company.activity_id = activity.id and country.id = company_country.country_id and company.id = company_country.company_id
        and country.iso = '%s'
        """ % (id))

    def getCancerNew_map(self, id):
        return self.sqlQueryS("""
        select country.iso as 'iso',country.name as `pays`, cancer.value as `nbr_cancer`, cancer.year as `stat_year`
from country, cancer where country.id = cancer.country_id and country.iso = '%s'
""" % (id))

    def getAlcoholNew_map(self, id):
        return self.sqlQueryS("""
        select country.iso as 'iso',country.name as `pays`,
alcohol.amount as `alc`, alcohol.date as `stat_year`
from country, alcohol where country.id = alcohol.country_id and country.iso = '%s'
""" % (id))

    def getKidnapNew_map(self, id):
        return self.sqlQueryS("""
        select country.iso as 'iso',country.name as `pays`,
kidnap.Amount as `kidnap`, kidnap.Date as `stat_year`
from country, kidnap where country.id = kidnap.Country and country.iso = '%s'
""" % (id))

    def getCinemaNew_map(self, id):
        return self.sqlQueryS("""
        select country.iso as 'iso',country.name as `pays`,
price_cinema.Amount as `cinema`, price_cinema.Date as `stat_year`
from country, price_cinema where country.id = price_cinema.country_id and country.iso = '%s'
""" % (id))

    # technical aspect
    # don't touch pls

    # Execute an SQL query and returns the result
    def sqlQuery(self, q):
        res = self.cur.execute(q)
        return self.cur.fetchall()

    def sqlQueryS(self, q):
        res = self.cur.execute(q)
        return self.cur.fetchall()
