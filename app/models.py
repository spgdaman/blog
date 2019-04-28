from . import db

class Quotes:


    def __init__(self,author,id,quote,permalink):
        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = permalink



class Users:
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username =db.Column(db.String(40), unique=True, index=True)
    email = db.Column(db.Dtring(255), unique=True, index=True)
    pass_hash = db.Column()