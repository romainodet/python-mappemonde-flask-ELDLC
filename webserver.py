from model import Model
from flask import *

# Create flask application
app = Flask(__name__)


# Define all routes (URL)

# defintion de la page d'accueil
@app.route('/')  # / is the URL
@app.route('/index.html')  # / is the URL
@app.route('/accueil/')  # / is the URL
def index():
    with Model() as model:
        country = model.getCountryNew()  # appel de la reqeute sql
    return render_template('index.html', country=country)  # afficher la page index html


# afficher la page qui liste tout les pays
@app.route('/info_country/')
def info_country():
    with Model() as model:
        # Get the artists as a list of dictionaries
        countries = model.getInfoCountry()  # sql pour obtenir tout les pays
        return render_template('info_country.html', countries=countries)  # afficher la page


# afficher un pays en particulier
@app.route('/info_country/<id>/')
def onlyCountry(id):
    with Model() as model:
        # appel sql des infos sur le pays et les infos sur la monnaie
        info = model.getInfoOnlyCountry(id)
        monnaie = model.getMonnaie(id)
        return render_template('country_one.html', info=info, monnaie=monnaie)  # afficher la page


# Afficher la liste des entreprises pour tous les pays
@app.route('/companies/')
def info_companies():
    with Model() as model:
        # sql pour obtenir toutes les entreprises
        companies = model.getCompanies()
        return render_template('companies.html', companies=companies)  # afficher la page


# afficher la liste des pays avec le nombre de cancers
@app.route('/cancer/')
def info_cancer():
    with Model() as model:
        # SQL pour obtenir le ombre de cancer par pays
        cancer = model.getCancer()
        return render_template('cancer.html', cancer=cancer)  # afficher la page


# afficher la liste des pays avec le taux d'alcool
@app.route('/alcool/')
def info_alcool():
    with Model() as model:
        # sQL pour obtenir le taux
        alcool = model.getAlcohol()
        return render_template('alchool.html', alcool=alcool)  # afficher la page


# affciher le nombre de kidnapping par pays
@app.route('/kidnap/')
def info_kidnap():
    with Model() as model:
        # SQl pour obtenir le nombre de kidnapping
        kidnap = model.getKidnap()
        return render_template('kidnap.html', kidnap=kidnap)  # afficher la page


# afficher le prix d'une place de cinéma par pays
@app.route('/cinema/')
def info_cinema():
    with Model() as model:
        # SQL pour obtenir la valeur
        cinema = model.getCinema()
        return render_template('cinema.html', cinema=cinema)  # afficher la page


# display a country when you use the slider
@app.route('/display_country.html')
def All_Countries():
    with Model() as model:
        # Get the artists as a list of dictionaries
        id = request.args.get('id')

        getInfoOnlyCountryNew = model.getInfoOnlyCountryNew(id)

        getMonnaieNew = model.getMonnaieNew(id)

        getCompanyNew = model.getCompanyNew(id)

        getCancerNew = model.getCancerNew(id)

        getAlcoholNew = model.getAlcoholNew(id)

        getKidnapNew = model.getKidnapNew(id)

        getCinemaNew = model.getCinemaNew(id)

        return render_template('display_country.html', country=getInfoOnlyCountryNew, monnaie=getMonnaieNew,
                               company=getCompanyNew, cancer=getCancerNew, alcool=getAlcoholNew,
                               kidnap=getKidnapNew, cinema=getCinemaNew)  # afficher la page


# new routes should be defined here

# show a country when click on the map
@app.route('/display_country_map.html')
def All_Countries_Map():
    with Model() as model:
        id = request.args.get('id')

        getInfoOnlyCountryNew = model.getInfoOnlyCountryNew_map(id)

        getMonnaieNew = model.getMonnaieNew_map(id)

        getCompanyNew = model.getCompanyNew_map(id)

        getCancerNew = model.getCancerNew_map(id)

        getAlcoholNew = model.getAlcoholNew_map(id)

        getKidnapNew = model.getKidnapNew_map(id)

        getCinemaNew = model.getCinemaNew_map(id)

        return render_template('display_country_map.html', country=getInfoOnlyCountryNew, monnaie=getMonnaieNew,
                               company=getCompanyNew, cancer=getCancerNew, alcool=getAlcoholNew,
                               kidnap=getKidnapNew, cinema=getCinemaNew)  # afficher la page


# main application
if __name__ == '__main__':
    # under windows, there is a bug in a module which prevents the usage of debug=True
    # the bug should be fixed within days or weeks, but in the meantime do not enable debug
    app.run(host='127.0.0.1', debug=True)
