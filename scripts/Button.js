import * as React from 'react';

import { Socket } from './Socket';

export class Button extends React.Component {
    constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
    handleSubmit(event) {
        event.preventDefault();
        FB.getLoginStatus((response) => {            
            if (response.status == 'connected') {                
                Socket.emit('new chat', {                    
                    'facebook_user_token': response.authResponse.accessToken,                    
                    'chat': this.state.value,
                    
                });  
                console.log(this.state.value);
            }        
        });
        
        let auth2 = gapi.auth2.getAuthInstance();
        let user = auth2.currentUser.get();
        if (user.isSignedIn()) {  
        
                console.log("yup"); 
                console.log(user.getAuthResponse().id_token);
                
                Socket.emit('new chat google', {     
                    'google_user_token': user.getAuthResponse().id_token,
                    'gID': auth2.currentUser.get().getId(),
                    'chat': this.state.value,
                    
                }); 
                 console.log("coolio");
                
            }
        
        console.log('Sent up the chat to server!', this.state.value);

        
    }
    
    
    
    handleChange(event) {
    this.setState({value: event.target.value});
  }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
             
                <input type="text" value={this.state.value} onChange={this.handleChange} />
                <button>Send!</button>
            </form>
        );
    }
}
