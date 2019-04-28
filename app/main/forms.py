from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email,EqualTo
from config import Config



class SignupForm(FlaskForm):
    firstname = StringField('First name: ', validators=[DataRequired()])
    lastname = StringField('Last name: ', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm')])
    pass_confirm = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')
