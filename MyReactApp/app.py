import os
import flask
import flask_socketio
import requests
import flask_sqlalchemy


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

import models 

# # URI scheme: postgresql://<username>:<password>@<hostname>:<port>/<database-name> 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://proj2_user:project2handin1@localhost/postgres'  
# db = flask_sqlalchemy.SQLAlchemy(app)



# clients = 0;

all_chats = [];
all_online_users = [];
@app.route('/')
def hello():
    
    # user = models.Message.query.filter_by(user='Natsu Dragneel').first()
    # print "image: " + user.img
    # print "name : " + user.user
    
    # msg = models.Message('pic.jpg', 'Natsu Dragneel', 'Rawr')
    # models.db.session.add(msg)
    # models.db.session.commit()
    return flask.render_template('index.html')
    


@socketio.on('connect')
def on_connect():
    socketio.emit('connection', { 
        'connected': 'Guest has connected'
        }, broadcast=True)
    # print " WHAT THE HELL???"
    chats = models.Message.query.all()
    del all_chats[:]
    for user in chats:
        all_chats.append({        
            'name': user.user,        
            'picture': user.img,        
            'chat': user.chat, 
            'fbID': user.fbID,
        })
        # print " TST "
        # print "all: " + user.img + " " + user.user + " " + user.chat
    socketio.emit('allchats', { 
        'chats': all_chats,
        # 'users': all_online_users,
        # 'onlineNum': len(all_online_users),
    }, broadcast=True)
    
    users = models.Users.query.all()
    del all_online_users[:]
    for user in users:
        all_online_users.append({        
            'name': user.user,        
            'picture': user.img,        
            'fbID': user.fbID,   
        })
    for user in all_online_users:
        print "TESTING2 " + user['name']
    socketio.emit('allusers', { 
        'users': all_online_users,
        'onlineNum': len(all_online_users),
        # 'users': all_online_users,
        # 'onlineNum': len(all_online_users),
    }, broadcast=True)
    # print " before "
    # for chat in all_chats:
    #     print chat["name"];
    #     print chat['picture']
    #     print chat['chat']
    
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
    # print "image: " + json['picture']['data']['url']
    msg = models.Message(json['picture']['data']['url'], json['id'], json['name'], data['chat'])
    models.db.session.add(msg)
    models.db.session.commit()
    # print "chat: " + data['chat'];
    # for num in all_chats:
    #     print num["chat"] + "yay"
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
    # print "fb connected";
    flag = False;
    
    
    users = models.Users.query.all()
    all_online_users = []
    del all_online_users[:]
    for user in users:
        all_online_users.append({        
            'name': user.user,        
            'picture': user.img,        
            'fbID': user.fbID,   
        })
    
    
    print "Logged in user: " + json['name']
    for user in users:
        print "pirnt: " + user.user;
        if (user.user == json['name']):
            flag = True;
    if (flag == False):
        all_online_users.append({
                'name': json['name'],        
                'picture': json['picture']['data']['url'], 
            })
        for usr in all_online_users:
            print "all online: " + usr['name']
        usr = models.Users(json['picture']['data']['url'], json['id'], json['name'])
        models.db.session.add(usr)
        models.db.session.commit()
    socketio.emit('fbConn', { 
        'users': all_online_users,
        'onlineNum': len(all_online_users),
        }, broadcast=True)
        
@socketio.on('fbDisconnected')
def fbDisconnection(data):
    print "USERID: " + data['userID']
    offlineUser = models.Users.query.filter_by(fbID=data['userID']).first();
    models.db.session.delete(offlineUser)
    models.db.session.commit()
    
    users = models.Users.query.all()
    # all_online_users = []
    del all_online_users[:]
    for user in users:
        all_online_users.append({        
            'name': user.user,        
            'picture': user.img,        
            'fbID': user.fbID,   
        })
    
    socketio.emit('allusers', { 
        'users': all_online_users,
        'onlineNum': len(all_online_users),
        # 'users': all_online_users,
        # 'onlineNum': len(all_online_users),
    }, broadcast=True)
    
   

    

if __name__ == '__main__':  # __name__!
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

