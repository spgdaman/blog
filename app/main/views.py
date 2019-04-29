from flask import render_template, flash, abort, request, url_for, redirect
from ..requests import get_random_quote
from . import main
from .forms import SignupForm, NewpostForm
from ..models import User,Post
from .. import db
import datetime 

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
        username=form.username.data, email=form.email.data, pass_hash=form.password.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)

@main.route('/posts', methods=["GET","POST"])
def show_all_posts():
    all_posts = Post.query.all()

    return render_template('allposts.html', all_posts=all_posts)

@main.route('/add/new_post', methods=["GET","POST"])
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














