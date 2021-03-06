import * as React from 'react';

import { Socket } from './Socket';

export class LogoutGoogle extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
        'buttonName': 'Google Logout',
    }

    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
  componentDidMount() {
      
  }
    
    handleSubmit(event) {
        event.preventDefault();
        var auth2 = gapi.auth2.getAuthInstance();
        Socket.emit('gDisconnected', {                    
                    'userID': auth2.currentUser.get().getId(),
                });
        auth2.signOut().then(function () {
          console.log('User signed out.');
        
        });
        

        
        
        

        console.log('The link was clicked.');
    }
    
    
    
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button id="gLogout">{this.state.buttonName}</button>
                
            </form>
        );
    }
}
