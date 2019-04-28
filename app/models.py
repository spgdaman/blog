from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quotes:


    def __init__(self,author,id,quote,permalink):
        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = permalink



class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    username =db.Column(db.String(40), unique=True, index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    pass_hash = db.Column(db.String(255))

    posts = db.relationship('Post',backref='user',lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("You cannot read password attribute")

    @password.setter
    def set_password(self, password):
        self.pass_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash_pass, password)

    def __repr__(self):
        return f"User {self.username}"

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    post_content = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_date = db.Column(db.DateTime)

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment_content = db.Column(db.String())
    post_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
