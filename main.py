import sqlite3
import numpy as np
from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
engine = create_engine("sqlite:///database.sqlite")

Base = declarative_base()


class Spotify(Base):
    __tablename__ = 'spotify'
    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)

app = Flask(__name__, static_folder='static')

@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/Stars")
def Stars():
    return render_template("Spotify Star Ratings.html")
@app.route("/Popularity")
def Popularity():
    return render_template("Popularity.html")

@app.route("/Tempo")
def Tempo():
    return render_template("Tempo.html")





@app.route("/Data", methods=["GET"])
def get_data():
    conn = sqlite3.connect("spotify_database.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM spotify_analytics")  
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return jsonify(data)
@app.route("/CountryData", methods=["GET"])
def get_country_data():
    conn = sqlite3.connect("spotify_database.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Country_Popularity")  
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return jsonify(data)
@app.route("/HipHopData", methods=["GET"])
def get_HipHop_data():
    conn = sqlite3.connect("spotify_database.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HipHOP_Popularity")  
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return jsonify(data)
@app.route("/IndiePopData", methods=["GET"])
def get_IndiePop_Data():
    conn = sqlite3.connect("spotify_database.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IndiePop_Popularity")  
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return jsonify(data)
@app.route("/PopData", methods=["GET"])
def get_Pop_Data():
    conn = sqlite3.connect("spotify_database.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pop_Popularity")  
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]
    conn.close()
    return jsonify(data)






@app.route("/Pop")
def Pop():
    return render_template("index.html")
@app.route("/HipHop")
def HipHop():
    return render_template("index.html")
@app.route("/Country")
def Country():
    return render_template("index.html")
@app.route("/IndiePop")
def IndiePop():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)