import * as React from 'react';

import { Socket } from './Socket';

export class Users extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            // numberOnline: 0,
        };
        
    }

    componentDidMount() {
    //   Socket.on('connection', (data) => {
            
    //         this.setState((prevState) => ({
    //             // 'newPerson': data['connected'],
    //             numberOnline: prevState.numberOnline + 1,
    //         }));
    //     })
    }
    // <p>People online: {this.state.numberOnline}</p>
    render() {
        
        return (
            <div>
                
            </div>
        );
    }
}
