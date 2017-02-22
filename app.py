import os
import flask
import flask_socketio
import requests
import flask_sqlalchemy
# from flask import jsonify
from flask import request



app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

import models 

# # URI scheme: postgresql://<username>:<password>@<hostname>:<port>/<database-name> 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://proj2_user:project2handin1@localhost/postgres'  
# db = flask_sqlalchemy.SQLAlchemy(app)



# clients = 0;

ip = [];
all_chats = [];
all_online_users = [];
all_possible_online_users = [];
chatBotImg = 'https://lh4.googleusercontent.com/vnCZbUminSYgNXsQdiQffUnjXa0XMnIS0_rqkynkjZb5_dM8jVfvAN68MuCRRCC4HYYMxXgp=s50-h50-e365'
# chatBotImg = 'http://a.deviantart.net/avatars/s/a/sandara.jpg'
    
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
    print "SOMEONE CONNECTED"
    # print request.sid
    # print request.remote_addr
    # print request.headers.getlist("X-Forwarded-For")[0]
    # # print " WHAT THE HELL???"
    
    # flagIP = False;
    # ips = models.ipAddr.query.all()
    # for usrs in ips:
    #     if (usrs.ip == request.sid):
    #         flagIP = True;
    # if (flagIP == False):
    #     ips.append({
    #             'ip': request.sid,  
    #         })
    #     users = models.Users.query.all()
    #     flagC = False;
    #     for u in users:
    #         if u.ip == request.sid:
    #             flagC = True;
    #     if  flagC == False:
    #         all_chats.append({        
    #             'name': 'Dragon-bot',        
    #             'picture': chatBotImg,        
    #             'chat': 'Watch out! Guest has connected!',   
    #         })
    #         msg = models.Message(chatBotImg, '1', 'Dragon-bot', 'Watch out! Guest has connected!')
    #         models.db.session.add(msg)
    #         models.db.session.commit()
            
    #     socketio.emit('all chats', { 
    #         'chats': all_chats,
    #         # 'users': all_online_users,
    #         # 'onlineNum': len(all_online_users),
    #     }, broadcast=True)
    #     socketio.emit('guestCo', { 
    #         # 'users': all_online_users,
    #         # 'onlineNum': len(all_online_users),
    #     }, broadcast=True)
    #     msg = models.ipAddr(request.sid)
    #     models.db.session.add(msg)
    #     models.db.session.commit()
    
    
    
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
    
    # print request.sid
    users = models.Users.query.all()
    
    for u in users:
        if u.ip == request.sid:
            
            print u.user + " disconnected"
            print u.fbID;
            socketio.emit('left', { 
                'user': u.fbID,
                # 'disconnected': 'Guest has disconnected',
                # 'left': True,
                })
        
    #     all_possible_online_users.append(u.ip);
    
    # # for pos in all_possible_online_users:
    # #     print pos["ip"] + " ID"
        
    # for i in range(len(all_possible_online_users)):
    #     print all_possible_online_users[i] + "ID"
        
    # online = False;
    # for i in range(len(all_possible_online_users)):
    #     print all_possible_online_users[i] + "ID during"
    #     if all_possible_online_users[i] == request.sid:
    #         all_possible_online_users.remove(request.sid)
    
    print "DISCONNECTED: " + request.sid
        
    
    # for i in range(len(all_possible_online_users)):
    #     print all_possible_online_users[i] + "ID AFTER"
    
    # socketio.emit('connectionLost', { 
    #     'disconnected': 'Guest has disconnected',
    #     'left': True,
    #     }, broadcast=True)
        
        
    # clients-=1;
    # socketio.emit('broadcast',{ description: clients + ' clients connected!'});
    
    
# @socketio.on('onlineCurrUser')
# def online_user(data):
#     all_possible_online_users = all_online_users;
    
#     for pos in all_possible_online_users:
#         print pos['fbID'] + " ID"
        
#     for user in all_possible_online_users:
#         if user['fbID'] == data['userID']:
#             all_possible_online_users.remove(data['userID'])
    
#     for pos in all_possible_online_users:
#         print pos['fbID'] + " ID AFTER"
    
#     socketio.emit('onlineUsers', {                    
#         'possible': all_possible_online_users,    
        
#     });



@socketio.on('new chat')
def on_new_chat(data):
    response = requests.get( 
        'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])    
    json = response.json()
    print json["id"]
    # print json.dumps(json, indent=2)
    
    
    if data['chat'].find("!!", 0, 2) != -1:
        print " DRAGON "
        if data['chat'].find("!! say", 0, 6) != -1:
            botChat = data['chat'][7:]
        else:
            if data['chat'] == "!! about":
                botChat = "Hello! I am Dragon-bot. This is a fun place to chat."
            elif data['chat'] == "!! help":
                botChat = "!! about \n!! help \n!! say \n!! rawr \n!! eat"
            elif data['chat'] == "!! rawr":
                botChat = "RAAAAWR!!!"
            elif data['chat'] == "!! eat":
                botChat = "FREE FOOD! Thank you!"
            else:
                botChat = "Nope! Check out !! help"
        all_chats.append({        
            'name': 'Dragon-bot',        
            'picture': chatBotImg,        
            'chat': botChat,   
        })
        msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat)
        models.db.session.add(msg)
        models.db.session.commit()
        # socketio.emit('chatBot', { 
        #     'chatBotMsg': botChat,
        #     # 'users': all_online_users,
        #     # 'onlineNum': len(all_online_users),
        # })
    else:
        all_chats.append({        
        'name': json['name'],        
        'picture': json['picture']['data']['url'],        
        'chat': data['chat'],   
        })
        msg = models.Message(json['picture']['data']['url'], json['id'], json['name'], data['chat'])
        models.db.session.add(msg)
        models.db.session.commit()
    socketio.emit('all chats', { 
        'chats': all_chats,
        # 'users': all_online_users,
        # 'onlineNum': len(all_online_users),
    }, broadcast=True)
    
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
    
    
    
    botChat = 'Welcome, ' + json['name'] + '! Say hi, everyone!!!'
    all_chats.append({        
        'name': 'Dragon-bot',        
        'picture': chatBotImg,        
        'chat': botChat,   
    })
    msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat)
    models.db.session.add(msg)
    models.db.session.commit()
    
    socketio.emit('all chats', { 
        'chats': all_chats,
        # 'users': all_online_users,
        # 'onlineNum': len(all_online_users),
    }, broadcast=True)
    
    socketio.emit('guestDis', { 
            # 'users': all_online_users,
            # 'onlineNum': len(all_online_users),
        }, broadcast=True)
    
    users = models.Users.query.all()
    # all_online_users = []
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
        usr = models.Users(json['picture']['data']['url'], json['id'], json['name'], request.sid)
        models.db.session.add(usr)
        models.db.session.commit()
    socketio.emit('fbConn', { 
        'users': all_online_users,
        'onlineNum': len(all_online_users),
        }, broadcast=True)
        

@socketio.on('gConnect')
def gConnection(data):
    response = requests.get( 
    'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])    
    json = response.json()
    print json["email"] + " email?"
    print "test"
    # print data['google_user_token'] + " google"
    print "Got an event for new number with data:", data
    
    botChat = 'Welcome, ' + json['name'] + '! Say hi, everyone!!!'
    all_chats.append({        
        'name': 'Dragon-bot',        
        'picture': chatBotImg,        
        'chat': botChat,   
    })
    msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat)
    models.db.session.add(msg)
    models.db.session.commit()
    
    socketio.emit('all chats', { 
        'chats': all_chats,
        # 'users': all_online_users,
        # 'onlineNum': len(all_online_users),
    }, broadcast=True)
    
    users = models.Users.query.all()
    # all_online_users = []
    del all_online_users[:]
    for user in users:
        all_online_users.append({        
            'name': user.user,        
            'picture': user.img,        
            'fbID': user.fbID,   
        })
        
    flag = False;
    print "Logged in user: " + json['name']
    for user in users:
        print "pirnt: " + user.user;
        if (user.user == json['name']):
            flag = True;
    if (flag == False):
        all_online_users.append({
                'name': json['name'],        
                'picture': json['picture'],
            })
        for usr in all_online_users:
            print "all online: " + usr['name']
        usr = models.Users(json['picture'], data['gID'], json['name'], request.sid)
        models.db.session.add(usr)
        models.db.session.commit()
        
        socketio.emit('gConn', { 
        'users': all_online_users,
        'onlineNum': len(all_online_users),
        }, broadcast=True)
    
    # socketio.emit('gConn', { 
    #     # 'users': all_online_users,
    #     # 'auth2': data['auth2'],
    #     })
    
@socketio.on('gLoggedIn')
def gLog(data):
    print " GOOOOOOGLE"
    print data['gUser']
    socketio.emit('gLoggedInBack', {
            'gUser': data['gUser'],
        });
        
@socketio.on('fbDisconnected')
def fbDisconnection(data):
    print "USERID: " + data['userID']
    offlineUser = models.Users.query.filter_by(fbID=data['userID']).first();
    discUser = offlineUser.user;
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
    
    botChat = 'Aww! ' + discUser + ' left us...'
    all_chats.append({        
        'name': 'Dragon-bot',        
        'picture': chatBotImg,        
        'chat': botChat,   
    })
    msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat)
    models.db.session.add(msg)
    models.db.session.commit()
    
    socketio.emit('all chats', { 
        'chats': all_chats,
        # 'users': all_online_users,
        # 'onlineNum': len(all_online_users),
    }, broadcast=True)
    
 

@socketio.on('gDisconnected')
def gDisconnection(data):
    print "USERID G: " + data['userID']
    offlineUser = models.Users.query.filter_by(fbID=data['userID']).first();
    discUser = offlineUser.user;
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
    
    botChat = 'Aww! ' + discUser + ' left us...'
    all_chats.append({        
        'name': 'Dragon-bot',        
        'picture': chatBotImg,        
        'chat': botChat,   
    })
    msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat)
    models.db.session.add(msg)
    models.db.session.commit()
    
    socketio.emit('all chats', { 
        'chats': all_chats,
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

