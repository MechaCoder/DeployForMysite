'use strict'

var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');

gulp.task('sass', function(){
    return gulp.src('./static/a/src/scss/*.scss')
        .pipe( sass().on('error', sass.logError) )
        .pipe( gulp.dest('./static/a/dist/css') )
});

gulp.task('sass:watch', function(){
    gulp.watch('./static/a/src/scss/**/*.scss', ['sass'])
});

gulp.task('build', function(){
    return gulp.src([
            "./node_modules/jquery/dist/jquery.min.js"
        ])
        .pipe( concat('main.js') )
        .pipe( gulp.dest('./static/a/dist/js/') )
});

gulp.task('default', ['build', 'sass']);
