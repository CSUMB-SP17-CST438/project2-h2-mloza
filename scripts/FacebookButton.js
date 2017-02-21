import * as React from 'react';

import { Socket } from './Socket';

export class FacebookButton extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
        'buttonName': 'Facebook Login',
    }

    this.handleSubmit = this.handleSubmit.bind(this);
    this.signIn = this.signIn.bind(this);
  }
  
  componentDidMount() {
    //   FB.getLoginStatus((response) => {            
    //     if (response.status == 'connected') {                
    //       console.log("logged in");
    //       this.setState({
    //             'buttonName': 'Facebook Logout',
    //         });
        // } else  {
        //     this.setState({
        //         'buttonName': 'Facebook Login',
        //     });
        // }        
    // }); 
  }
  
    handleSubmit(event) {
        event.preventDefault();
        FB.login(function(response) {
            if (response.authResponse) {
             console.log('Welcome!  Fetching your information.... ');
             FB.api('/me', function(response) {
               console.log('Good to see you, ' + response.name + '.');
               FB.getLoginStatus((response) => {            
                    if (response.status == 'connected') {                
                        Socket.emit('fbConnected', {                    
                            'facebook_user_token': response.authResponse.accessToken,  
                        });  
                    }        
                });
            //   Socket.emit('fbConnected', {                    
            //         'facebook_user_token': response.authResponse.accessToken,
                    
            //     }); 
               this.setState({
                    'buttonName': 'Facebook Logout',
                });
             });
            } else {
             console.log('User cancelled login or did not fully authorize.');
            //  this.setState({
            //     'buttonName': 'Facebook Login',
            // });
            }
        });
        console.log('Sent up the chat to server!');
    }
    
    signIn(e) {
    e.preventDefault();
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
            'auth2': auth2,
            // 'facebook_user_token': '',                  
            
        });                
        
    } 
    console.log(user);
    auth2.signIn().then(function () {
      console.log('User signed in.');
    });

    console.log('The link was clicked.');
  }
    
    
    
    render() {
        return (
            <div>
            <form onSubmit={this.handleSubmit}>
                <button id="fbLogin">{this.state.buttonName}</button>
            </form>
            <a href="#" onClick={this.signIn}>Sign in</a>
            </div>
        );
    }
}
