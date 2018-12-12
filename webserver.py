from model import Model
from flask import *

# Create flask application
app = Flask(__name__)


# Define all routes (URL)

@app.route('/')  # / is the URL
@app.route('/index.html')  # / is the URL
@app.route('/accueil/')  # / is the URL
def index():
    # These log messages are just to show you how you can use them to debug your application
    with Model() as model:
        country = model.getCountryNew()
    return render_template('index.html', country=country)


# Show artists (simple case)
@app.route('/info_country/')
def info_country():
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        countries = model.getInfoCountry()
        return render_template('info_country.html', countries=countries)

# Show single artist
@app.route('/info_country/<id>/')
def onlyCountry(id):
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        info = model.getInfoOnlyCountry(id)
        monnaie = model.getMonnaie(id)
        return render_template('country_one.html', info=info , monnaie=monnaie)


# Show artists (simple case)
@app.route('/companies/')
def info_companies():
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        companies = model.getCompanies()
        return render_template('companies.html', companies=companies)


# Show artists (simple case)
@app.route('/cancer/')
def info_cancer():
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        cancer = model.getCancer()
        return render_template('cancer.html', cancer=cancer)


# Show artists (simple case)
@app.route('/alcool/')
def info_alcool():
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        alcool = model.getAlcohol()
        return render_template('alchool.html', alcool=alcool)


# Show artists (simple case)
@app.route('/kidnap/')
def info_kidnap():
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        kidnap = model.getKidnap()
        return render_template('kidnap.html', kidnap=kidnap)


@app.route('/cinema/')
def info_cinema():
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        cinema = model.getCinema()
        return render_template('cinema.html', cinema=cinema)
# new routes should be defined here


# Show single artist
@app.route('/display_country.html')
def All_Countries():
    # This is needed to use the query defined in the model.py module
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
        print(getCompanyNew)
        return render_template('display_country.html', country=getInfoOnlyCountryNew, monnaie=getMonnaieNew,
                               company=getCompanyNew, cancer=getCancerNew, alcool=getAlcoholNew,
                               kidnap=getKidnapNew, cinema=getCinemaNew)

# new routes should be defined here

# main application
if __name__ == '__main__':
    # under windows, there is a bug in a module which prevents the usage of debug=True
    # the bug should be fixed within days or weeks, but in the meantime do not enable debug
    app.run(host='127.0.0.1', debug=True)
