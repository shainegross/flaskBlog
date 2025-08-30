from flask import Blueprint
from flask import render_template, request, Blueprint
from flaskBlog.models import Posts

main = Blueprint('main', __name__)


@main.route("/")
def home():
    page=request.args.get('page', 1, type=int)
    posts = Posts.query.order_by(Posts.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html",posts=posts)

@main.route("/about")
def about():
    return render_template("about.html", title = 'About')

@main.route('/favicon.ico')
def favicon():
    return '', 204  # Suppress favicon 404

