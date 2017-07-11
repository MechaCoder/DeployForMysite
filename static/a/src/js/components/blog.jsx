import * as React from 'react';
import * as ReactDom from 'react-dom';

import {makeAjaxCall} from './utills.jsx';

var FontAwesome = require('react-fontawesome');
var Md = require('react-markdown');

export class Blog_page extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            title: '',
            content: ''
        };

        this.clickbutton = this.clickbutton.bind(this);
    }

    clickbutton(){

        var contentDict = makeAjaxCall(
            '/ajax/blog/post/',
            {'post_id': this.state.curPost}
        );

        this.setState({
            title: contentDict.title,
            content: contentDict.content
        });

        return false;
    }

    post(arg){

        return(<div className='post'>
            <div className='post-title' >{arg.post_title}</div>
            <div className='post-content hide' >{arg.post}</div>
            <div className='post-date' >{arg.date}</div>
            <div className='tool-bar' >
                <button onClick={()=>{
                    this.state.curPost = arg.id;
                    this.clickbutton();
                }}>
                    <FontAwesome name="newspaper-o"/>
                </button>
            </div>
        </div>);
    }

    render() {

        var posts = [];


        for(var i = 0; i < this.props.content.length; i++){
            posts.push( this.post(this.props.content[i]) );
        }

        return(<div>
            <div className="post-list" >{posts}</div>
            <BlogPost_display title={this.state.title} content={this.state.content} />
        </div>);
    }

}

class BlogPost_display extends React.Component {
    constructor(props){
        super(props);
    }

    render(){
        return(
            <div className="display">
                <div className="display-title">{this.props.title}</div>
                <div className="display-content"><Md source={this.props.content} /></div>
            </div>
        );
    }
}