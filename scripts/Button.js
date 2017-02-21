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
        // Socket.emit('new number', {
        //     'number': this.state.value,
        // });
        console.log('Sent up the chat to server!', this.state.value);

        // let random = Math.floor(Math.random() * 100);
        // console.log('Generated a random number: ', random);
        // Socket.emit('new number', {
        //     'number': random,
        // });
        // console.log('Sent up the random number to server!');
    }
    
    // <textarea value={this.state.value} onChange={this.handleChange} cols="30" rows="5" ></textarea>
    
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
