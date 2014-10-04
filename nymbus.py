import os
from flask import Flask, request, jsonify

app = Flask(__name__)

handshakes = []
profiles = {'nymi_id': 'www.nymion.herokuapp.com'}

@app.route('/')
def index():
    return "Hello World"

@app.route('/new-handshake', methods = ['POST'])
def new_handshake():
    if not request.headers['Content-Type'] == 'application/json':
        return 
    handshake = {'nymi_id': request.json['nymi_id'], 
            'timestamp': request.json['timestamp']} 
    handshakes.append(handshake)
    return jsonify({'handshake': handshake}), 201

@app.route('/get-handshake')
def get_handshake():
    handshake = request.json['handshake']
    if handshake == 0:
        return jsonify({'status': 'not-ok'})
    profile_url = profiles[long(handshake['nymi_id'])]
    return jsonify({'status': 'ok',
                    'profile': profile_url})
    
def find_profile(handshake):
    handshake_ts = long(handshake['timestamp'])
    for hs in handshakes:
        time_diff = handshake_ts - long(hs['timestamp'])
        if abs(time_diff) < 5000
            return hs
    return 0
