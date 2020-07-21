import os

from flask import Flask
from flask import request

import json

app = Flask(__name__)

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
            ret = sensor_put()
        else:
            ret = ('Method Not Allowed', 405)
    
    # Send Return
    print('sensor: ', ret)
    return ret

def sensor_get(dev_id):
    return ({'id': dev_id, 'temp': 25, 'humid': 75}, 200)

def sensor_put():
    print('sensor_put')
    return ('PUT', 200)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))