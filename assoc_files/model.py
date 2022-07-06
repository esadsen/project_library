from assoc_files.config import db
from sqlalchemy.orm import backref






class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    auth = db.Column(db.Integer)
    email = db.Column(db.String(45))


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    isbn = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
