from flask import render_template, flash, abort, request, url_for, redirect
from ..requests import get_random_quote
from . import main
from .forms import SignupForm
from ..models import User,Post
from .. import db

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

@main.route('/posts' methods=["GET","POST"])
def show_all_posts():
    all_posts = Post.query.all()

    db.session.add(all_posts)
    db.session.commit()

    return render_template('index.html', all_posts=all_posts)














