from flask import render_template, redirect, url_for, flash
from . import auth
from .forms import LoginForm

@auth.route('/login')
def login():
    form = LoginForm()

    if form.validate_on_submit():
        pass
    return render_template('auth/login.html')