import * as React from 'react';

import { Users } from './Users';
import { Button } from './Button';
import { FacebookButton } from './FacebookButton';
import { GoogleButton } from './GoogleButton';
import { Logout } from './Logout';
import { Socket } from './Socket';

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            // 'chats': '',
            'chats': [],
            'newPerson': '',
            'personLeft': '',
            'users': [],
            'onlineNum': 0,
            'testChat': [],
            'testUser': [],
            'testOnlineNum': 0,
            'possibleOffline': [],
            'chatBot': '',
            'guestNu': 0,
        };
        // Socket.on('allchats', (data) => {
        //     this.setState({
        //         'testChat': data['chats'],
        //         // 'users': data['users'],
        //         // 'onlineNum': data['onlineNum'],
        //     });
        // })
        this.signOut = this.signOut.bind(this);
         
    }
    
//     function signOut() {
//     var auth2 = gapi.auth2.getAuthInstance();
//     auth2.signOut().then(function () {
//       console.log('User signed out.');
//     });
//   }


signOut(e) {
    e.preventDefault();
    var auth2 = gapi.auth2.getAuthInstance();
    console.log(auth2);
    let user = auth2.currentUser.get();
    if (user.isSignedIn()) {  
        console.log(auth2.currentUser.get().getId() + "id go");
        var profile = auth2.currentUser.get().getBasicProfile();
        console.log('ID dis: ' + profile.getId());         
        
    } 
    auth2.signOut().then(function () {
      console.log('User signed out.');
    //   console.log(auth2.currentUser.get().getId() + "id out");
    });
    if (user.isSignedIn()) {  
        console.log(auth2.currentUser.get().getId() + "id go");
        var profile = auth2.currentUser.get().getBasicProfile();
        console.log('ID dis: ' + profile.getId());         
        
    } else {
        console.log("out");
    }
    console.log('The link was clicked.');
  }

    componentDidMount() {
        
        
        
//         function signOut() {
//     var auth2 = gapi.auth2.getAuthInstance();
//     auth2.signOut().then(function () {
//       console.log('User signed out.');
//     });
//   }

        
//         gapi.signin2.render('g-signin2', {
//     'scope': 'https://www.googleapis.com/auth/plus.login',
//     'width': 200,
//     'height': 50,
//     'longtitle': true,
//     'theme': 'dark',
//     'onsuccess': this. onSignIn
//   });  
        
        Socket.on('all chats', (data) => {
            this.setState({
                // 'chats': data['chats'],
                // 'users': data['users'],
                // 'onlineNum': data['onlineNum'],
                'testChat': data['chats'],
                
            });
            // console.log(this.);
        
        })
        
        Socket.on('guestCo', (data) => {
            this.setState({
                // 'chats': data['chats'],
                // 'users': data['users'],
                // 'onlineNum': data['onlineNum'],
                'guestNu': this.state.guestNu + 1,
                
            });
            // console.log(this.);
        
        })
        
        Socket.on('guestDis', (data) => {
            this.setState({
                // 'chats': data['chats'],
                // 'users': data['users'],
                // 'onlineNum': data['onlineNum'],
                'guestNu': this.state.guestNu - 1,
                
            });
            // console.log(this.);
        
        })
        
        Socket.on('left', (data) => {
            // this.setState({
            //     'guestNu': this.state.guestNu - 1,
                
            // });
            FB.getLoginStatus((response) => {            
                if (response.status == 'connected') {  
                // userID = response.authResponse.userID;
                //   console.log(response.authResponse.userID);
                //   console.log(response.authResponse.accessToken);
                    Socket.emit('fbDisconnected', {                    
                        'userID': data['user'],
                    });
                  console.log("test");
                }        
            });
            
            FB.logout(function(response) {
              // user is now logged out
            });
            // console.log(this.);
        
        })
        
        // Socket.on('chatBot', (data) => {
        //     this.setState({
        //         // 'chats': data['chats'],
        //         // 'users': data['users'],
        //         // 'onlineNum': data['onlineNum'],
        //         'chatBot': data['chatBot'],
                
        //     });
        //     // console.log(this.);
        
        // })
        
        Socket.on('allchats', (data) => {
            this.setState({
                'testChat': data['chats'],
                // 'users': data['users'],
                // 'onlineNum': data['onlineNum'],
            });
        })
        
        Socket.on('allusers', (data) => {
            this.setState({
                'testUser': data['users'],
                'testOnlineNum': data['onlineNum'],
                // 'users': data['users'],
                // 'onlineNum': data['onlineNum'],
            });
        })
        
        Socket.on('fbConn', (data) => {
            this.setState({
                'users': data['users'],
                'onlineNum': data['onlineNum'],
                
                'testUser': data['users'],
                'testOnlineNum': data['onlineNum'],
            });
            
        
        })
        
        Socket.on('gConn', (data) => {
            let user = data['auth2'].currentUser.get();
            if (user.isSignedIn()) {  
                console.log("working");
                console.log(data['auth2'].currentUser.get().getId() + "id go");
                var profile = data['auth2'].currentUser.get().getBasicProfile();
                console.log('ID: ' + profile.getId());
                console.log('Full Name: ' + profile.getName());
                console.log('Image URL: ' + profile.getImageUrl());
                       
                
            } 
            // this.setState({
            //     'users': data['users'],
            //     'onlineNum': data['onlineNum'],
                
            //     'testUser': data['users'],
            //     'testOnlineNum': data['onlineNum'],
            // });
            
        
        })
        
        FB.getLoginStatus((response) => {            
            if (response.status == 'connected') {                
               console.log("logged in");
            }        
        });
        
        
        Socket.on('connectionLost', (data) => {
            
            this.setState({
                'personLeft': data['disconnected']
            });
            
            // FB.getLoginStatus((response) => {            
            //     if (response.status == 'connected') {                
            //       Socket.emit('onlineCurrUser', {                    
            //         'userID': response.authResponse.userID,    
                    
            //     });
            //     }        
            // });
              
            
        })
        
        
        // Socket.on('onlineUsers', (data) => {
        //   this.setState({
        //         'possibleOffline': data['possible']
        //     });
        
        //     console.log("first test");
        
        //     FB.getLoginStatus((response) => {            
        //         if (response.status == 'connected') {                
        //             for (i = 0; i < possibleOffline.length; i++) {
        //                 console.log("testing loop");
        //                 if (response.authResponse.userID == possibleOffline[i]) {
        //                     Socket.emit('fbDisconnected', {                    
        //                         'userID': response.authResponse.userID,
        //                     });
        //                     // FB.logout(function(response) {
        //                     //   // user is now logged out
        //                     // });
        //                     console.log("DISCONNECTED");
        //                 }
        //             }
        //         }
        
        //     }); 
            
        // })
        
        
    }
    // <p>{this.state.newPerson}</p> 
// <p>{this.state.chats}</p>
    render() {
        // let chats = this.state.chats.map(
        //     (n, index) => <li key={index}>{n}</li>
        // );
        let chats = this.state.chats.map((n, index) =>            
            <li key={index}>                
                <img src={n.picture} />                
                {n.name}: {n.chat}            
            </li>        
        );
        
        let testChat = this.state.testChat.map((n, index) =>            
            <li key={index}>                
                <img src={n.picture} />   
                {n.name}: {n.chat}            
            </li>        
        );
        let testUser = this.state.testUser.map((n, index) =>            
            <li key={index}>     
                <img src={n.picture} />                
                {n.name}            
            </li>        
        );
        
        let users = this.state.users.map((n, index) =>            
            <li key={index}>     
                Online ({this.state.onlineNum}):
                <img src={n.picture} />                
                {n.name}            
            </li>        
        );
        
        // <ul>{users}</ul>
        //         <ul id="allChat">{testChat}</ul>
        //         <ul id="newChat">{chats}</ul>
        //         <ul id="onlineUsers">{testUser}</ul>
        
        // <div                    
        //             className="fb-login-button"                    
        //             data-max-rows="1"                    
        //             data-size="medium"                    
        //             data-show-faces="false"                   
        //             data-auto-logout-link="true">                
        //         </div>
        
        // <p>Guests({this.state.guestNu})</p>
        return (
            <div>
                <Users />
                <h1>Chating...</h1>
                
                
                <p>{this.state.personLeft}</p> 
                
                <FacebookButton />
                <GoogleButton />
                <Logout />
                <div 
                    className="g-signin2" 
                    data-theme="dark"> 
                </div>
                <a href="#" onClick={this.signOut}>Sign out</a>

               

                
                    <div id="chat">
                        <ul id="allChat">{testChat}</ul>
                    </div>
                    <div id="users">
                        <p id="noMarg">Online now ({this.state.testOnlineNum}): </p>
                        <ul id="onlineUsers">{testUser}</ul>  
                    </div>
                    <div id="clear"></div>
            
                
                
                <Button />
            </div>
        );
    }
}