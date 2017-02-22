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
        var flag = false;
        let auth2 = gapi.auth2.getAuthInstance();
        
        auth2.signIn().then(function() {
            console.log(auth2.currentUser.get().getId());
            console.log("working");
            let user = auth2.currentUser.get();
            if (user.isSignedIn()) {  
        
                console.log("yup"); 
                console.log(user.getAuthResponse().id_token);
                
                Socket.emit('gConnect', {                        
                    'google_user_token': user.getAuthResponse().id_token, 
                    'gID': auth2.currentUser.get().getId(),
                    'gLoginFlag': true,
                    // 'facebook_user_token': '',                  
                    
                }); 
                 console.log("cool");
                
            } 
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
