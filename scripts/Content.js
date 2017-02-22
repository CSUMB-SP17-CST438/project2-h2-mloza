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
            'fbLoginFlag': false,
            'gLoginFlag': false,
        };
         
    }
    


    componentDidMount() {
        
        
        
        Socket.on('logFB', (data) => {
            this.setState({
                'fbLoginFlag': data['fbLoginFlag'],
                
            });
             console.log(this.state.gLoginFlag);
            console.log(this.state.fbLoginFlag);
        
        })
        
        console.log(this.state.gLoginFlag);
            console.log(this.state.fbLoginFlag);
        
        Socket.on('logG', (data) => {
            this.setState({
                'gLoginFlag': data['gLoginFlag'],
                
            });
             console.log(this.state.gLoginFlag);
            console.log(this.state.fbLoginFlag);
        
        })
        
        Socket.on('all chats', (data) => {
            this.setState({
                'testChat': data['chats'],
                
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
        
       
        
        
        
        
        
        
    }
    
    render() {
        

        
        
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