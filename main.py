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

@app.route('/rap')
def rap():

    return render_template('rap.html')

@app.route('/pop')
def pop():

    return render_template('pop.html')

@app.route('/rock')
def hip_hop():

    return render_template('rock.html')

@app.route('/country')
def country():

    return render_template('country.html')