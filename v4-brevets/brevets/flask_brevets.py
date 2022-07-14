"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import Flask, redirect, url_for, request, abort, render_template
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


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
    app.logger.debug("beg_date={}".format(beg_date))
    app.logger.debug("beg_time={}".format(beg_time))
    
    beg_dateAndTime = beg_date + ' ' + beg_time
    #beg_dateAndTime = arrow.get(beg_date + ' ' + beg_time, 'YYYY-MM-DD HH:mm').isoformat()
    #print(beg_dateAndTime)
    open_time = acp_times.open_time(km, brev_dist, beg_dateAndTime)
    close_time = acp_times.close_time(km, brev_dist, beg_dateAndTime)
    rslt = {"open": open_time, "close": close_time, "beg_date": beg_date, "beg_time": beg_time}
    return flask.jsonify(result=rslt)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
