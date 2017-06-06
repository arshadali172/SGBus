#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response
import datetime
# from time import gmtime, strftime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):

    if req.get("result").get("action") != "nextBusUpdate":
        return {}

    result = req.get("result")
    parameters = result.get("parameters")
    busstopid = parameters.get("bus-stop-id")

    uri = 'http://datamall2.mytransport.sg/'
    path = 'ltaodataservice/BusArrival?'
    specifics = 'BusStopID=' + busstopid + '&SST=True'

    query = Request(uri + path + specifics)
    query.add_header('AccountKey', [INSERT DATAMALL ACOUNT KEY])
    query.add_header('accept', 'application/json')
    result = urlopen(query).read()
    data = json.loads(result)

    speech = generateResponse(data, parameters.get("bus-no"))

    return {
        "speech": speech
    }

def generateResponse(data, buses):

    services = ''
    to_add = ''
    curTime = datetime.datetime.utcnow()
    
    all_buses = False
    count = 0
    if len(buses) == 0:
        all_buses = True

    for bus in data['Services']:

        bus_no = bus['ServiceNo'] 
        time_str = bus['NextBus']['EstimatedArrival']

        if len(time_str) > 0 and (int(bus_no) in buses or all_buses is True):
            services += to_add
            busTime = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S+08:00')
            time_str = str(int((busTime - curTime).total_seconds()/60 - 8*60))
            count += 1
        else:
            continue

        to_add = ', a bus '+ bus_no + ' in ' + time_str + ' minutes' 

    if count == 1:
        services += to_add
    elif count > 1:
        services += ' and ' + to_add
    else:
        return 'I could not find any buses at bus stop ' + " ".join(data['BusStopID'])
    return 'At bus stop ' + " ".join(data['BusStopID']) + ' there is ' + services


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')



