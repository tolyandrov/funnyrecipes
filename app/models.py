from app import db
from datetime import datetime

ROLE_USER = 0
ROLE_ADMIN = 1

# class Recipe(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     body = db.Column(db.String(140))
#
#     def __repr__(self):
#         return '<Recipe %r>' % (self.body)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)

    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

class Recipe(db.Model):

    __tablename__ = "recipes"
    id = db.Column('recipe_id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(500), unique=False, index=True)
    body = db.Column('body', db.String(5000))
    def __init__(self, title, body):
        self.title = title
        self.body = body