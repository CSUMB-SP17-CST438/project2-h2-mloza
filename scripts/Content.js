import * as React from 'react';

import { Users } from './Users';
import { Button } from './Button';
import { FacebookButton } from './FacebookButton';
import { GoogleButton } from './GoogleButton';
import { Logout } from './Logout';
import { LogoutGoogle } from './LogoutGoogle';
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
         
    }
    


    componentDidMount() {
        
        
       

        

        
        Socket.on('all chats', (data) => {
            this.setState({
                'testChat': data['chats'],
                
            });
        
        })
        
        Socket.on('guestCo', (data) => {
            this.setState({
                'guestNu': this.state.guestNu + 1,
                
            });
        
        })
        
        Socket.on('guestDis', (data) => {
            this.setState({
                'guestNu': this.state.guestNu - 1,
                
            });
        
        })
        
        Socket.on('left', (data) => {
            FB.getLoginStatus((response) => {            
                if (response.status == 'connected') {  
                    Socket.emit('fbDisconnected', {                    
                        'userID': data['user'],
                    });
                  console.log("test");
                }        
            });
            
            FB.logout(function(response) {
              // user is now logged out
            });
        
        })
        
        
        
        Socket.on('allchats', (data) => {
            this.setState({
                'testChat': data['chats'],
            });
        })
        
        Socket.on('allusers', (data) => {
            this.setState({
                'testUser': data['users'],
                'testOnlineNum': data['onlineNum'],
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
                       
                
            this.setState({
                'testUser': data['users'],
                'testOnlineNum': data['onlineNum'],
            });
            
            
            
        
        })
        
       
        
        
        Socket.on('connectionLost', (data) => {
            
            this.setState({
                'personLeft': data['disconnected']
            });
            
            
              
            
        })
        
        
        
        
        
    }
    
    render() {
        
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
        
        
        return (
            <div>
                <Users />
                <h1>Chating...</h1>
                
                
                <p>{this.state.personLeft}</p> 
                
                <FacebookButton />
                <GoogleButton />
                <Logout />
                <LogoutGoogle />
                <div 
                    className="g-signin2" 
                    data-theme="dark"> 
                </div>

               

                
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