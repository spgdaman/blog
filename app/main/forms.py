from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email,EqualTo
from wtforms import ValidationError
from config import Config
from ..models import User, Post, Comment


class SignupForm(FlaskForm):
    firstname = StringField('First name: ', validators=[DataRequired()])
    lastname = StringField('Last name: ', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Sign up')

class NewpostForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    content = StringField(validators=[DataRequired()])
    post = SubmitField('post')
