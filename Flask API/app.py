from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour la section Étudiant
@app.route('/etudiant')
def etudiant():
    return render_template('etudiant.html')

# Route pour la section Professeur
@app.route('/professeur')
def professeur():
    return render_template('professeur.html')

# Route pour la section Administration
@app.route('/administration')
def administration():
    return render_template('administration.html')


