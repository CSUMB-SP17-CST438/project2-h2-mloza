import * as React from 'react';

import { Socket } from './Socket';

export class FacebookButton extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
        'buttonName': 'Facebook Login',
    }

    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
  componentDidMount() {
    
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
               this.setState({
                    'buttonName': 'Facebook Logout',
                });
             });
            } else {
             console.log('User cancelled login or did not fully authorize.');
            
            }
        });
        console.log('Sent up the chat to server!');
    }
    
    


    
    
    
    render() {
        return (
            <div>
            <form onSubmit={this.handleSubmit}>
                <button id="fbLogin">{this.state.buttonName}</button>
            </form>
            </div>
        );
    }
}
