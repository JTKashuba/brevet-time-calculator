"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import Flask, redirect, url_for, request, abort, render_template
import arrow  # Replacement for datetime, based on moment.js
import os
import acp_times  # Brevet time calculations
import config
from pymongo import MongoClient

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb


###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    db.controlPoints.drop()
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


#@app.route("/_submit", methods=["POST"])
@app.route("/submitDatabase")
def submit_db():
    """
    Submits open/close times to mongodb database
    """
    km = request.args.get('km', type=float)
    open_time_field = request.args.get('open_time_field', type=str)
    close_time_field = request.args.get('close_time_field', type=str)
    item_doc = {
        'km': km,
        'open_time_field': open_time_field,
        'close_time_field': close_time_field
    }
    db.controlPoints.insert_one(item_doc)

    rslt = {"km": km, "open_time": open_time_field, "close_time": close_time_field}
    return flask.jsonify(result=rslt)



#@app.route("/_display", methods=["POST"])
@app.route("/displayDatabase")
def display_db():
    """
    Redirects the user the a new page displaying the
    control open/close times stored in the database
    """
    _items = db.controlPoints.find()
    items = [item for item in _items]

    return render_template('display.html', items=items)



###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', type=float)
    brev_dist = request.args.get("brev_dist", type=float)
    beg_date = request.args.get('beg_date', type=str)
    beg_time = request.args.get('beg_time', type=str)
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    #print("Calculated beg_date as: " + beg_date)
    #naively trying to see output^, should be following syntax from above like this:
    app.logger.debug("beg_date={}".format(beg_date))
    app.logger.debug("beg_time={}".format(beg_time))

    #beg_dateAndTime = beg_date + ' ' + beg_time + ':00'
    beg_dateAndTime = beg_date + ' ' + beg_time
    #date_time_arrow = arrow.get(beg_dateAndTime, 'YYYY-MM-DD HH:mm:ss')
    #beg_dateAndTime = arrow.get(beg_date + ' ' + beg_time, 'YYYY-MM-DD HH:mm')
    #beg_dateAndTime = arrow.get(beg_date + ' ' + beg_time, 'YYYY-MM-DD HH:mm').isoformat()

    open_time = acp_times.open_time(km, brev_dist, beg_dateAndTime)
    close_time = acp_times.close_time(km, brev_dist, beg_dateAndTime)
    result = {"open": open_time, "close": close_time, "beg_date": beg_date, "beg_time": beg_time}
    #result = {"open": open_time, "close": close_time, "beg_dateAndTime": beg_dateAndTime}
    return flask.jsonify(result=result)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
