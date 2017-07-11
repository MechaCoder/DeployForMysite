import * as React from 'react';
import * as ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom';

import {Renderpage} from './components/page.jsx';
import {Blog_page} from './components/blog.jsx';
import {Interactive_cv} from './components/cv.jsx';
import {makeAjaxCall} from './components/utills.jsx';


var page = 'main';
if(location.search.split('?').length === 2){
    page = location.search.split('?')[1];
}

var content = '';
if(page === 'blog'){
    content = makeAjaxCall('/ajax/blog/', {});
} else {
    content = makeAjaxCall('/ajax/', {'name': page});
}

const display_main = () =>  (
    <Renderpage content={content} />
);

const display_blog = () => (
    <Blog_page content={content} />
);


ReactDOM.render(
    <Router>
        <Route path="" component={display_main} />
        <Route path="?main" component={display_main} />
        <Route path="?pofile" component={display_main} />
        <Route path="?blog" component={display_blog} />
    </Router>,
    document.getElementById('app_root')
);