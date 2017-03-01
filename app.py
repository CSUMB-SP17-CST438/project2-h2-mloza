import os
import flask
import flask_socketio
import requests
import flask_sqlalchemy
from flask import request
from urlparse import urlparse
import re
import imghdr
import requests_oauthlib
import json
import random


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

import models 


ip = [];
all_chats = [];
all_online_users = [];
all_possible_online_users = [];
imageType = ["png", "PNG", "jpg", "JPG", "jpeg", "JPEG", "gif", "GIF"]
imgType = ["image/jpeg", "image/png", "image/gif"]
chatBotImg = 'https://lh4.googleusercontent.com/vnCZbUminSYgNXsQdiQffUnjXa0XMnIS0_rqkynkjZb5_dM8jVfvAN68MuCRRCC4HYYMxXgp=s50-h50-e365'
# chatBotImg = 'http://a.deviantart.net/avatars/s/a/sandara.jpg'
    
@app.route('/')
def hello():
    return flask.render_template('index.html')
    


@socketio.on('connect')
def on_connect():
    print "SOMEONE CONNECTED"
    
    
    
    
    chats = models.Message.query.all()
    del all_chats[:]
    for user in chats:
        all_chats.append({        
            'name': user.user,        
            'picture': user.img,        
            'chat': user.chat, 
            'fbID': user.fbID,
            'url': user.url,
        })
    # print all_chats
    socketio.emit('allchats', { 
        'chats': all_chats,
        
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
    }, broadcast=True)
    
    
    print "sent"


@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'
    
    # print request.sid
    users = models.Users.query.all()
    
    for u in users:
        if u.ip == request.sid:
            
            print u.user + " disconnected"
            print u.fbID;
        
    
    
    print "DISCONNECTED: " + request.sid
        
    
@socketio.on('new chat google')
def on_new_chat_google(data):
    response = requests.get( 
    'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])    
    json = response.json()
    
    
    if data['chat'].find("!!", 0, 2) != -1:
        print " DRAGON "
        if data['chat'].find("!! say", 0, 6) != -1:
            botChat = data['chat'][7:]
        else:
            if data['chat'] == "!! about":
                botChat = "Hello! I am Dragon-bot. This is a fun place to chat."
            elif data['chat'] == "!! help":
                botChat = "!! about \n!! help \n!! say \n!! rawr \n!! eat \n!! food <type> <location>"
            elif data['chat'] == "!! rawr":
                botChat = "RAAAAWR!!!"
            elif data['chat'] == "!! food":
                botChat = "coming soon"
            elif data['chat'] == "!! eat":
                botChat = "FREE FOOD! Thank you!"
            else:
                botChat = "Nope! Check out !! help"
        all_chats.append({        
            'name': 'Dragon-bot',        
            'picture': chatBotImg,        
            'chat': botChat,   
            'url': '',
        })
        msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat, '')
        models.db.session.add(msg)
        models.db.session.commit()
    else:
        all_chats.append({        
        'name': json['name'],        
        'picture': json['picture'],        
        'chat': data['chat'],   
        'url': '',
        })
        msg = models.Message(json['picture'], data['gID'], json['name'], data['chat'], '')
        models.db.session.add(msg)
        models.db.session.commit()
    socketio.emit('all chats', { 
        'chats': all_chats,
    }, broadcast=True)
    
    print "Got an event for new google with data:", data    





@socketio.on('new chat')
def on_new_chat(data):
    response = requests.get( 
        'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])    
    json = response.json()
    print json["id"]
    
    posURL = urlparse(data['chat'])  
    # if posURL.scheme or posURL.netloc:
    #     # valid url
    #     print posURL.scheme + " " + posURL.netloc + " url"
    #     all_chats.append({        
    #     'name': json['name'],        
    #     'picture': json['picture']['data']['url'],        
    #     'chat':  data['chat'],   
    #     })
    #     msg = models.Message(json['picture']['data']['url'], json['id'], json['name'], data['chat'], 'U')
    #     models.db.session.add(msg)
    #     models.db.session.commit()
        
    
    if data['chat'].find("!!", 0, 2) != -1:
        # print " DRAGON "
        if data['chat'].find("!! say", 0, 6) != -1:
            botChat = data['chat'][7:]
        else:
            if data['chat'] == "!! about":
                botChat = "Hello! I am Dragon-bot. This is a fun place to chat."
            elif data['chat'] == "!! help":
                botChat = "!! about \n!! help \n!! say \n!! rawr \n!! eat\n!! food <type> <location>"
            elif data['chat'] == "!! rawr":
                botChat = "RAAAAWR!!!"
            elif data['chat'] == "!! eat":
                botChat = "FREE FOOD! Thank you!"
            elif data['chat'] == "!! food":
                botChat = "coming soon"
                url = "https://api.yelp.com/v2/search?term=sushi&location=Monterey, CA&limit=40" 
                oauth = requests_oauthlib.OAuth1(
                    'P9HpnKvg3flN6o1KrsHgxw', 
                    'uJm6epI8CUT968OQc_8K0xBR9PQ',
                    'eCEh6_yEE7S1i0r3h7GNO-CIF_llaDOb',
                    'V_SBhCGKhBruxND3mswQC1pYCYE'
                )
                response = requests.get(url, auth=oauth)
                json_body = response.json()
                randNum = random.randint(0, 39) #only 40 hits are returned
                name = json_body["businesses"][randNum]["name"]
                yelpURL = json_body["businesses"][randNum]["url"]
                phone = json_body["businesses"][randNum]["display_phone"]
                foodStreet = json_body["businesses"][randNum]["location"]["display_address"][0]
                foodCity = json_body["businesses"][randNum]["location"]["display_address"][1]
                botChat = yelpURL
                all_chats.append({        
                    'name': 'Dragon-bot',        
                    'picture': chatBotImg,        
                    'chat': botChat,   
                    'url': 'U',
                })
                msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat, 'U')
                models.db.session.add(msg)
                models.db.session.commit()
                botChat = name + " " + foodStreet + " " + foodCity + " " + phone
                # print json_body
                # print "LOCATION: " + foodStreet + " " + foodCity
            else:
                botChat = "Nope! Check out !! help"
        all_chats.append({        
            'name': 'Dragon-bot',        
            'picture': chatBotImg,        
            'chat': botChat,   
            'url': '',
        })
        msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat, '')
        models.db.session.add(msg)
        models.db.session.commit()
    elif posURL.scheme or posURL.netloc:
        image = requests.head(data['chat'])
        posImg = image.headers.get('content-type')
        if (posImg == "image/gif" or posImg == "image/png" or posImg == "image/jpeg"):
            print "image"
            all_chats.append({        
                'name': json['name'],        
                'picture': json['picture']['data']['url'],        
                'chat':  data['chat'], 
                'url': 'I',
            })
            msg = models.Message(json['picture']['data']['url'], json['id'], json['name'], data['chat'], 'I')
            models.db.session.add(msg)
            models.db.session.commit()
        else:
            # print posURL.scheme + " " + posURL.netloc + " url"
            all_chats.append({        
                'name': json['name'],        
                'picture': json['picture']['data']['url'],        
                'chat':  data['chat'], 
                'url': 'U',
            })
            msg = models.Message(json['picture']['data']['url'], json['id'], json['name'], data['chat'], 'U')
            models.db.session.add(msg)
            models.db.session.commit()
    else:
        all_chats.append({        
        'name': json['name'],        
        'picture': json['picture']['data']['url'],        
        'chat': data['chat'],
        'url': '',
        })
        msg = models.Message(json['picture']['data']['url'], json['id'], json['name'], data['chat'], '')
        models.db.session.add(msg)
        models.db.session.commit()
    # print all_chats
    socketio.emit('all chats', { 
        'chats': all_chats,
    }, broadcast=True)
    
    print "Got an event for new number with data:", data
    
    
@socketio.on('fbConnected')
def fbConnection(data):
    response = requests.get( 
    'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])    
    json = response.json()
    flag = False;
    
    
    botChat = 'Welcome, ' + json['name'] + '! Say hi, everyone!!!'
    all_chats.append({        
        'name': 'Dragon-bot',        
        'picture': chatBotImg,        
        'chat': botChat,  
        'url': '',
    })
    msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat, '')
    models.db.session.add(msg)
    models.db.session.commit()
    
    socketio.emit('all chats', { 
        'chats': all_chats,
    }, broadcast=True)
    
    
    users = models.Users.query.all()
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
    print "Got an event for new number with data:", data
    
    
    botChat = 'Welcome, ' + json['name'] + '! Say hi, everyone!!!'
    all_chats.append({        
        'name': 'Dragon-bot',        
        'picture': chatBotImg,        
        'chat': botChat,  
        'url': '',
    })
    msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat, '')
    models.db.session.add(msg)
    models.db.session.commit()
    
    socketio.emit('all chats', { 
        'chats': all_chats,
    }, broadcast=True)
    
    users = models.Users.query.all()
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
    
  
    
@socketio.on('gLoggedIn')
def gLog(data):
    print " GOOOOOOGLE"
    print data['gUser']
    
        
@socketio.on('fbDisconnected')
def fbDisconnection(data):
    print "USERID: " + data['userID']
    offlineUser = models.Users.query.filter_by(fbID=data['userID']).first();
    discUser = offlineUser.user;
    models.db.session.delete(offlineUser)
    models.db.session.commit()
    
    
    users = models.Users.query.all()
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
    }, broadcast=True)
    
    botChat = 'Aww! ' + discUser + ' left us...'
    all_chats.append({        
        'name': 'Dragon-bot',        
        'picture': chatBotImg,        
        'chat': botChat, 
        'url': '',
    })
    msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat, '')
    models.db.session.add(msg)
    models.db.session.commit()
    
    socketio.emit('all chats', { 
        'chats': all_chats,
    }, broadcast=True)
    
 

@socketio.on('gDisconnected')
def gDisconnection(data):
    print "USERID G: " + data['userID']
    offlineUser = models.Users.query.filter_by(fbID=data['userID']).first();
    discUser = offlineUser.user;
    models.db.session.delete(offlineUser)
    models.db.session.commit()
    
    
    users = models.Users.query.all()
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
    }, broadcast=True)
    
    botChat = 'Aww! ' + discUser + ' left us...'
    all_chats.append({        
        'name': 'Dragon-bot',        
        'picture': chatBotImg,        
        'chat': botChat,   
        'url': '',
    })
    msg = models.Message(chatBotImg, '1', 'Dragon-bot', botChat, '')
    models.db.session.add(msg)
    models.db.session.commit()
    
    socketio.emit('all chats', { 
        'chats': all_chats,
    }, broadcast=True)
    
    

if __name__ == '__main__':  # __name__!
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

