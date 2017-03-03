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
            'testChat': [],
            'testUser': [],
            'testOnlineNum': 0,
        };
         
    }
    


    componentDidMount() {
        
        gapi.load('auth2', function() {
            gapi.auth2.init();
        });
        
        
        
        Socket.on('all chats', (data) => {
            this.setState({
                'testChat': data['chats'],
                
            });
            // console.log(data['chats']);
            // console.log(this.state.testChat);
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
        
       
        
        
        
        
        
        
    }
    
    render() {
        let testChat = this.state.testChat.map(function(n, index) { 
                if (n.url == 'U') {
                    return <li key={index}>                
                        <img src={n.picture} /> 
                        {n.name}: <a href={n.chat} target="_blank">{n.chat}</a>
                                    
                    </li>  
                } else if (n.url == 'I') {
                    return <li key={index}>                
                        <img src={n.picture} /> 
                        {n.name}: <img src={n.chat} />
                                    
                    </li>
                }
                else {
                    return <li key={index}>                
                        <img src={n.picture} /> 
                        {n.name}: 
                        <span>{n.chat}</span>
                                    
                    </li> 
                }
                   
        }.bind(this));
        
        let testUser = this.state.testUser.map((n, index) =>            
            <li key={index}>     
                <img src={n.picture} />                
                {n.name}            
            </li>        
        );
        
        
        return (
            <div>
                <h1>Chatting...</h1>
                
                
                
                <FacebookButton />
                <GoogleButton />
                
                <Logout />
                <LogoutGoogle />
                

               

                
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