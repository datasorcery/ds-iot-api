import os
from os import path
import json
from datetime import datetime
import pytz

from flask import Flask
from flask import request

from google.cloud import firestore

app = Flask(__name__)

# Setup credential for local development
pwd = path.dirname(path.abspath(__file__))
local_credential_file = "{}/gcp.json".format(pwd)
if os.path.isfile(local_credential_file):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=local_credential_file

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    return 'Hello {}!\n'.format(target)

# GET /sensor/<id> -> Retorna última leitura do sensor
# PUT /sensor/<id> -> Salva leitura do sensor

@app.route('/sensor/<dev_id>', methods=['GET', 'PUT'])
def sensor(dev_id):
    """HTTP Cloud Funtion.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    #request_json = request.get_json(silent=True)
    #request_args = request.args

    # Check conditions and methods
    if dev_id is None:
        ret = ('Invalid ID', 400)
    else:
        if request.method == 'GET':
            ret = sensor_get(dev_id)
        elif request.method == 'PUT':
            ret = sensor_put(dev_id)
        else:
            ret = ('Method Not Allowed', 405)
    
    # Send Return
    print('sensor: ', ret)
    return ret

def sensor_get(dev_id):
    # Create Firestore Client
    db = firestore.Client()

    # Get data from this sensor
    sensor_ref = db.collection(u'nodemcu_TH_{}'.format(dev_id))
    sensor_docs = sensor_ref.stream()

    readings = list()

    for read in sensor_docs:
        readings.append(read.to_dict())

    return (json.dumps(readings), 200)
    #return ({'id': dev_id, 'temp': 25, 'humid': 75}, 200)

def sensor_put(dev_id):
    # Plumbing
    request_json = request.get_json(silent=True)
    
    # Create Firestore Client
    db = firestore.Client()

    # Document name -> time in YYYYMMDDHHMMSS GMT
    doc_name = datetime.now().astimezone(pytz.utc).strftime('%Y%m%d%H%M%S')

    # Add new reading 
    doc_ref = db.collection(u'nodemcu_TH_{}'.format(dev_id)).document(u'{}'.format(doc_name))
    doc_ref.set({
        u'temp': request_json['temp'],
        u'humid': request_json['humid'],
        u'timestamp': doc_name
    })
  
    print('sensor_put:', request_json['temp'], request_json['humid'])
    return ('OK', 200)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))