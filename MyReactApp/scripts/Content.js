import * as React from 'react';

import { Users } from './Users';
import { Button } from './Button';
import { Socket } from './Socket';

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            // 'numbers': '',
            'numbers': [],
            // 'newPerson': '',
            'personLeft': '',
        };
        //  Socket.on('allnumbers', (data) => {
        //     this.setState({
        //         'numbers': data['numbers']
        //     });
        // })
    }

    componentDidMount() {
        Socket.on('all numbers', (data) => {
            this.setState({
                'numbers': data['numbers']
            });
        })
        
        
        Socket.on('connectionLost', (data) => {
            
            this.setState({
                'personLeft': data['disconnected']
            });
        })
    }
    // <p>{this.state.newPerson}</p> 
// <p>{this.state.numbers}</p>
    render() {
        // let numbers = this.state.numbers.map(
        //     (n, index) => <li key={index}>{n}</li>
        // );
        let numbers = this.state.numbers.map((n, index) =>            
            <li key={index}>                
                <img src={n.picture} />                
                {n.name}: {n.number}            
            </li>        
        );
        return (
            <div>
                <Users />
                <h1>Random numbers so far! Yay!</h1>
                
                
                <p>{this.state.personLeft}</p> 
                <div                    
                    className="fb-login-button"                    
                    data-max-rows="1"                    
                    data-size="medium"                    
                    data-show-faces="false"                   
                    data-auto-logout-link="true">                
                </div>
                <Button />
                <ul>{numbers}</ul>
            </div>
        );
    }
}
