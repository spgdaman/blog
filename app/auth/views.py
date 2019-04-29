from flask import render_template, redirect, url_for, flash, request
from . import auth
from .forms import LoginForm
from flask_login import login_user,login_required, logout_user
from ..models import User

@auth.route('/login', methods=["GET","POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is not None and user.check_password(password=login_form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.show_all_posts'))
        else:
            flash('Invalid username or password')
        
    return render_template('auth/login.html',login_form=login_form)

@auth.route('/logout')
@login_required
def logout():
    logout()
    return redirect(url_for('main.index'))