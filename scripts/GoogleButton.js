import * as React from 'react';

import { Socket } from './Socket';

export class GoogleButton extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
        'buttonName': 'Google Login',
    }

    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
  componentDidMount() {
      
  }
  
    handleSubmit(event) {
        event.preventDefault();
        
        let auth2 = gapi.auth2.getAuthInstance();
        let user = auth2.currentUser.get();
        if (user.isSignedIn()) {  
            console.log(auth2.currentUser.get().getId() + "id go");
            var profile = auth2.currentUser.get().getBasicProfile();
            console.log('ID: ' + profile.getId());
            console.log('Full Name: ' + profile.getName());
            console.log('Image URL: ' + profile.getImageUrl());
    
    
            Socket.emit('gConnected', {                        
                'google_user_token': user.getAuthResponse().id_token,                        
                // 'facebook_user_token': '',                  
                
            });                
            
        } 
        console.log(user);
        auth2.signIn().then(function () {
          console.log('User signed in.');
        });

    console.log('The link was clicked.');
        console.log('Sent up the chat to server!');
    }
    
    
    
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button id="gLogin">{this.state.buttonName}</button>
                
            </form>
        );
    }
}
