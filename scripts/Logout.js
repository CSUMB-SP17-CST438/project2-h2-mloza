import * as React from 'react';

import { Socket } from './Socket';

export class Logout extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
        'buttonName': 'Facebook Logout',
        
    }

    this.handleSubmit = this.handleSubmit.bind(this);
  }
  

  componentDidMount() {
      
      
    
    
    
    
  }
  
    handleSubmit(event) {
        event.preventDefault();
        FB.getLoginStatus((response) => {            
            if (response.status == 'connected') {  
               console.log(response.authResponse.userID);
                Socket.emit('fbDisconnected', {                    
                    'userID': response.authResponse.userID,
                });
            }        
        });
        
        FB.logout(function(response) {
          // user is now logged out
        });
        console.log('logged out');
    }
    
    
    
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button id="fbLogout">{this.state.buttonName}</button>
            </form>
        );
    }
}
