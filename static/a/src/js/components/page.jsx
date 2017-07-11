import * as React from 'react';
var Md = require('react-markdown');


export class Renderpage extends React.Component {
    constructor(p){
        super(p);
    }
    render() {
        return (<div><Md source={this.props.content} /></div>);
    }


}
