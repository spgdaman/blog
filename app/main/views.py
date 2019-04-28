from flask import render_template, flash, abort, request, url_for, redirect
from ..requests import get_random_quote
from . import main
from .forms import SignupForm

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/random_quote')
def show_quote():
    quote = get_random_quote()
    return render_template('quotes.html',quotes=quote)

@main.route('/signup')
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)