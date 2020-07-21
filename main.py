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

@app.route('/sensor', methods=['GET', 'PUT'])
@app.route('/sensor/<id>', methods=['GET', 'PUT'])
def sensor(id=None):
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

    if id is not None:
        print('id')
        ret = {'id': id, 'temp': 25, 'humid': 75}
    else:
        ret = 'NO <ID>'

    return (ret, 200)

def sensor_get():
    pass

def sensor_put():
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))