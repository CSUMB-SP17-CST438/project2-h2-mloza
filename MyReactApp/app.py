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
    


all_chats = [];
all_online_users = [];
@socketio.on('new chat')
def on_new_chat(data):
    response = requests.get( 
        'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])    
    json = response.json()
    print json["id"]
    # print json.dumps(json, indent=2)
    all_chats.append({        
        'name': json['name'],        
        'picture': json['picture']['data']['url'],        
        'chat': data['chat'],   
    })
    print "chat: " + data['chat'];
    for num in all_chats:
        print num["chat"] + "yay"
    # flag = False;
    # for user in all_online_users:
    #     print user["name"];
    #     if (user["name"] == json['name']):
    #         flag = True;
    # if (flag == False):
    #     all_online_users.append({
    #             'name': json['name'],        
    #             'picture': json['picture']['data']['url'], 
    #         })
    # print json['name']
    print "Got an event for new number with data:", data
    # TODO: Fill me out!
    # all_chats.append(data['number'])
    socketio.emit('all chats', { 
        'chats': all_chats,
        # 'users': all_online_users,
        # 'onlineNum': len(all_online_users),
        }, broadcast=True)
    # socketio.emit('all numbers', { 
    #     'numbers': data['number']
    #     }, broadcast=True)
    
@socketio.on('fbConnected')
def fbConnection(data):
    response = requests.get( 
    'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])    
    json = response.json()
    print "fb connected";
    flag = False;
    for user in all_online_users:
        print user["name"];
        if (user["name"] == json['name']):
            flag = True;
    if (flag == False):
        all_online_users.append({
                'name': json['name'],        
                'picture': json['picture']['data']['url'], 
            })
    socketio.emit('fbConn', { 
        'users': all_online_users,
        'onlineNum': len(all_online_users),
        }, broadcast=True)

socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)


