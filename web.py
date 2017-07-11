
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from local_site import Html_lists
from local_site.sitedata import DataElemements
from local_site.blog import BlogWorker


app = Flask(__name__)


@app.route('/')
def index():
    app_asserts = Html_lists(
        [
            "./static/a/dist/js/main.js",
            "./static/a/dist/js/bundle.js",
            "https://use.fontawesome.com/450359af36.js"
        ],
        ["./static/a/dist/css/test.css"],
        DataElemements().get_nav()
    )

    return render_template(
        'base.html',
        pageTitle=DataElemements().get_siteTitle(),
        cssList=app_asserts.get_css(),
        jsList=app_asserts.get_js(),
        pageList=app_asserts.get_pages()
    )


@app.route('/ajax/', methods=['POST', 'GET'])
def ajax():
    pageName = request.form.get('name')
    return DataElemements().get_page(pageName)

@app.route('/ajax/blog/', methods=['POST'])
def ajax_blog():
    return jsonify(BlogWorker().get())


@app.route('/ajax/blog/post/', methods=['POST'])
def ajax_post():
    postid = request.form.get('post_id')

    return jsonify(BlogWorker().get_single(postid))


if __name__ == '__main__':
    app.run(debug=True)
