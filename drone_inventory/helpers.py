from functools import wraps

import secrets
import decimal
import requests

from flask import request, jsonify, json 

from drone_inventory.models import User

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split()[1]
            print(token)

        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        try:
            our_user = User.query.filter_by(token=token).first()
            print(our_user)
            if not our_user or our_user.token != token:
                return jsonify({'message': 'Token is invalid'})
            
        except:
            our_user = User.query.filter_by(token=token).first()
            if token != our_user.token and secrets.compare_digest(token, our_user.token):
                return jsonify({'message': 'Token is invalid'})
        return our_flask_function(our_user, *args, **kwargs)
    return decorated


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSONEncoder, self).default(obj)
    

    

def random_joke_generator():
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
        "X-RapidAPI-Key": "9b16110cdemsh97cefceb253d517p1e1aecjsn9ef744f7b15e",
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()

    return data['body'][0]['setup'] + ' ' + data['body'][0]['punchline']

