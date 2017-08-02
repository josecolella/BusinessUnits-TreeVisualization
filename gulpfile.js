const gulp = require('gulp');
const uglify = require('gulp-uglify-es').default;
const rename = require("gulp-rename");

gulp.task("uglify", function () {
    return gulp.src(["app/static/*.js", "!app/static/*.min.js"])
        .pipe(uglify())
        .pipe(rename({
            suffix: ".min"
        }))
        .pipe(gulp.dest("app/static/"));
});

gulp.task('default', ['minify'], function() {
    console.log("Finished");
});
