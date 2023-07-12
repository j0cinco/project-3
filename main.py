import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template

app = Flask(__name__)

engine = create_engine("sqlite:///data/table_schemata.sql")

def home():

    return render_template('home.html')

def rap():

    return render_template('rap.html')

@app.route('/pop')
def pop():

    return render_template('pop.html')

@app.route('/hiphop')
def hip_hop():

    return render_template('hiphop.html')

@app.route('/country')
def country():

    return render_template('country.html')

@app.route('/dubstep')
def dubstep():

    return render_template('dubstep.html')