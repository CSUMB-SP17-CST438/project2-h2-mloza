import * as React from 'react';

import { Users } from './Users';
import { Button } from './Button';
import { FacebookButton } from './FacebookButton';
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
        };
        // Socket.on('allchats', (data) => {
        //     this.setState({
        //         'testChat': data['chats'],
        //         // 'users': data['users'],
        //         // 'onlineNum': data['onlineNum'],
        //     });
        // })
         
    }

    componentDidMount() {
        Socket.on('all chats', (data) => {
            this.setState({
                // 'chats': data['chats'],
                // 'users': data['users'],
                // 'onlineNum': data['onlineNum'],
                'testChat': data['chats'],
                
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
                Test
                {n.name}: {n.chat}            
            </li>        
        );
        let testUser = this.state.testUser.map((n, index) =>            
            <li key={index}>     
                Online now ({this.state.testOnlineNum}):
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
        return (
            <div>
                <Users />
                <h1>Random numbers so far! Yay!</h1>
                
                
                <p>{this.state.personLeft}</p> 
                
                <FacebookButton />
                <Logout />
                
                
                <ul id="allChat">{testChat}</ul>
                <ul id="onlineUsers">{testUser}</ul>     
                <Button />
            </div>
        );
    }
}