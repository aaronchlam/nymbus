from flask import Flask, request, jsonify

app = Flask(__name__)

handshakes = []
profiles = {'1': {'url': 'http://nymion.herokuapps.com'},
            '2': {'url': 'http://nymion.herokuapps.com'}}
recent_handshakes = []

@app.route('/')
def index():
    return "Hello World"

#@app.route('/recent-handshakes')
#def recent_handshake():
#    nymi_id = request.json['nymi_id']
#    for hs in recent_handshakes:
#        if nymi_id == hs['nymi_id']:
#            continue
#       
#        

@app.route('/new-handshake', methods = ['POST'])
def new_handshake():
    if not request.headers['Content-Type'] == 'application/json':
        return error(404)
    handshake = {'nymi_id': request.json['nymi_id'], 
            'timestamp': request.json['timestamp']} 
    handshakes.append(handshake)
    return jsonify({'handshake': handshake}), 201

@app.route('/get-handshake', methods = ['POST'])
def get_handshake():
    handshake = find_profile(request.json['handshake'])
    if handshake == 0:
        return jsonify({'status': 'not-ok'})
    profile = profiles[handshake['nymi_id']]
    return jsonify({'status': 'ok',
                    'profile': profile['url']})
    
def find_profile(handshake):
    handshake_ts = long(handshake['timestamp'])
    for hs in handshakes:
        if hs['nymi_id'] == handshake['nymi_id']:
            continue
        time_diff = handshake_ts - long(hs['timestamp'])
        if abs(time_diff) < 5000:
            recent_handshakes.append(hs)
            return hs
    return 0

if __name__ == '__main__':
    app.run(debug=True)
