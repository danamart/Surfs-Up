from flask import Flask, jsonify
import datetime
from datetime import date, timedelta
import numpy as numpy
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func

engine = create_engine("sqlite://hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/precipitation")
#Convert the query results to a Dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.
def prcp():
    previous_year = dt.date.today() - dt.timedelta(days=365)
    prcp_year = session.query(measurement.date,func.sum(measurement.prcp)).filter(measurement.date >= previous_year).group_by(measurement.date).order_by(measurement.date).all()

    prcp_dict = dict(prcp_year)
    return jsonify(prcp_dict)



@app.route("/api/v1.0/stations")
#Return a JSON list of stations from the dataset
def stations():
    station_q = session.query(Station.station).all()
    station_list = list(np.ravel(station_q))
    return jsonify (station_list)


#@app.route("/api/v1.0/tobs")

#query for the dates and temperature observations from a year from the last data point.
#Return a JSON list of Temperature Observations (tobs) for the previous year.

#@app.route("/api/v1.0/<start>")
#@app.route("/api/v1.0/<start>/<end>")

#Return a JSON list of the minimum temperature, the average temperature, and the max 
#temperature for a given start or start-end range.
#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than 
#and equal to the start date.
#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates 
#between the start and end date inclusive.


if __name__ == "__main__":
    app.run(debug=True)