from model import Model
from flask import *

# Create flask application
app = Flask(__name__)


# Define all routes (URL)

@app.route('/')  # / is the URL
def index():
    # These log messages are just to show you how you can use them to debug your application

    return render_template('index.html')


# Show artists (simple case)
@app.route('/info_country.html')
def info_country():
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        countries = model.getInfoCountry()
        return render_template('info_country.html', countries=countries)

# Show single artist
@app.route('/onlyCountry/<id>')
def onlyCountry(id):
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        info = model.getInfoOnlyCountry(id)
        monnaie = model.getMonnaie(id)
        return render_template('country_one.html', info=info , monnaie=monnaie)


# Show artists (simple case)
@app.route('/companies.html')
def info_companies():
    # This is needed to use the query defined in the model.py module
    with Model() as model:
        # Get the artists as a list of dictionaries
        companies = model.getCompanies()
        return render_template('companies.html', companies=companies)



# new routes should be defined here


# main application
if __name__ == '__main__':
    # under windows, there is a bug in a module which prevents the usage of debug=True
    # the bug should be fixed within days or weeks, but in the meantime do not enable debug
    app.run(host='127.0.0.1', debug=True)
