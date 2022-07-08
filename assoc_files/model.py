from assoc_files.config import db
from sqlalchemy.orm import backref






class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    auth = db.Column(db.Integer)
    email = db.Column(db.String(45))
    books = db.Column(db.Integer)

class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    isbn = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    rent_date = db.Column(db.DateTime)
    last_rent_date = db.Column(db.DateTime)
    last_user = db.Column(db.Integer)
