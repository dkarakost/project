from . import db # importing the function from init.py line 3
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # the unique means that no user should have same email
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    notes = db.relationship('Note')


# all the above class is the user model
