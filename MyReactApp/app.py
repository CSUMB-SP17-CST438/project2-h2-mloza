import os
import flask
import flask_socketio
import requests

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

# clients = 0;

@app.route('/')
def hello():
    return flask.render_template('index.html')
    


@socketio.on('connect')
def on_connect():
    print 'Someone connected!!'
    socketio.emit('allnumbers', { 
        'numbers': all_numbers 
        
    })
    socketio.emit('connection', { 
        'connected': 'Guest has connected'
        }, broadcast=True)
    print "sent"
    # clients+=1;
    # socketio.emit('broadcast',{ description: clients + ' clients connected!'});
    

@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'
    socketio.emit('connectionLost', { 
        'disconnected': 'Guest has disconnected'
        }, broadcast=True)
    # clients-=1;
    # socketio.emit('broadcast',{ description: clients + ' clients connected!'});
    


all_numbers = [];
@socketio.on('new number')
def on_new_number(data):
    response = requests.get( 
        'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])    
    json = response.json()
    all_numbers.append({        
        'name': json['name'],        
        'picture': json['picture']['data']['url'],        
        'number': data['number'],    
    })
    print json['name']
    print "Got an event for new number with data:", data
    # TODO: Fill me out!
    # all_numbers.append(data['number'])
    socketio.emit('all numbers', { 
        'numbers': all_numbers
        }, broadcast=True)
    # socketio.emit('all numbers', { 
    #     'numbers': data['number']
    #     }, broadcast=True)

socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)


