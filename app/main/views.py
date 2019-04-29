from flask import render_template, flash, abort, request, url_for, redirect
from ..requests import get_random_quote
from . import main
from .forms import SignupForm, NewpostForm
from ..models import User,Post
from .. import db
import datetime
from flask_login import login_required
from werkzeug.security import generate_password_hash

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/random_quote')
def show_quote():
    quote = get_random_quote()
    return render_template('quotes.html',quotes=quote)

@main.route('/signup', methods=["GET","POST"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        user = User(firstname = form.firstname.data, lastname=form.lastname.data,
        username=form.username.data, email=form.email.data, pass_hash=generate_password_hash(form.password.data))

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)

@main.route('/posts', methods=["GET","POST"])
def show_all_posts():
    all_posts = Post.query.all()

    return render_template('allposts.html', all_posts=all_posts)

@main.route('/add/new_post', methods=["GET","POST"])
@login_required
def add_new():
    newpost_form = NewpostForm()
    timestamp = datetime.datetime.now().strftime("%d-%m-%y %H:%M")

    if newpost_form.validate_on_submit():

        post = Post(title=newpost_form.title.data ,post_content=newpost_form.content.data,post_date=timestamp)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('main.get_post',post_id=post.id))

    return render_template('newpost.html',newpost_form=newpost_form)

@main.route('/posts/<post_id>')
def get_post(post_id):
    post = Post.query.filter_by(id=post_id).first()

    return render_template('showpost.html',post=post)

@main.route('/delete/post/<post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first()

    if post.post_content is not None:
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('main.show_all_posts'))
    return None

# @main.route('/add/<post_id>/new_comment')
# def new_comment(post_id):
#     pass

@main.route('/profile/<user_id>')
def show_profile(user_id):
    user=User.query.filter_by(id=user_id).first()
    return render_template('profile.html',user=user)












