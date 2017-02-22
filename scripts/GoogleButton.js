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
                    // 'facebook_user_token': '',                  
                    
                }); 
                 console.log("cool");
                
            } 
          });

        
        // auth2.signIn().then(function () {
        //     let user = auth2.currentUser.get();
        //     if (user.isSignedIn()) {  
        
        //         console.log("yup");
        //         Socket.emit('gConnect', {                        
        //             'google_user_token': user.getAuthResponse().id_token, 
        //             // 'facebook_user_token': '',                  
                    
        //         });                
                
        //     } 
        //     console.log(user.getAuthResponse().id_token);
        //   console.log('User signed in.');
        // });
        // auth2.signIn();
        // console.log('User signed in.');
        
        
        
        // Socket.emit('gLoggedIn', {
        //     'gUser': user,
        // });
        
        
        

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
