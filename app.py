from flask import Flask, jsonify

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

############# Set Up the Database #############
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()

# reflect tables
Base.prepare(engine, reflect=True)
tables = Base.classes.keys()
print(tables)

# create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

############# Set Up Flask #############
app = Flask(__name__)

# Create the Welcome Route
@app.route("/")
def welcome():
    return('''
    Welcome to the Climate Analysis API!\n<br>
    Available Routes:\n<br>
    /api/v1.0/precipitation\n<br>
    /api/v1.0/stations\n<br>
    /api/v1.0/tobs\n<br>
    /api/v1.0/temp/start/end
    ''')
    