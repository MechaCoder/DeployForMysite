var webpack = require('webpack');
var path = require('path');

var dist = path.resolve(__dirname, 'static/a/dist/js');
var src = path.resolve(__dirname, 'static/a/src/js');

var config = {
  entry: src + '/index.jsx',
  output: {
    path: dist,
    filename: 'bundle.js'
  },
  module : {
    loaders : [
      {
        test : /\.jsx?/,
        include : src,
        loader : 'babel-loader'
      }
    ]
  }
};

module.exports = config;
