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
def index():
    return render_template("index.html")


@app.route("/data", methods=["GET"])
def get_data():
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM spotify")  
    rows = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]
    data = [dict(zip(columns, row)) for row in rows]

    conn.close()

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)