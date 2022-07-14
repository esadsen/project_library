from assoc_files.config import bcrypt
from assoc_files.config import app
from flask import Flask, flash, redirect,url_for, render_template, request , session
from assoc_files.model import User , Books
from assoc_files.config import db
from functools import wraps
from datetime import date, datetime
from sqlalchemy import *


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session : 
             return f(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return decorated_function



@app.route('/',methods = ['GET','POST'])
def home_route():
    return render_template("index.html")


@app.route("/home",methods = ['GET','POST'])
def home():
    return render_template("index.html")
    


@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            user = User.query.filter_by(username=username).first()
            #print(bcrypt.check_password_hash(user.password,password))
            if user.username == username and user.password==password:
                #routes pages
                if user.auth == 1:
                    session["admin"] = True
                    session["logged_in"] = True
                    session["user_id"] = user.id
                    return redirect(url_for("profile"))
                else:
                    session["logged_in"] = True
                    session["user_id"] = user.id
                    return redirect(url_for("book_page"))
        except:    
            return "auth failed"

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("home")


@app.route('/books')
@login_required
def book_page():

    books = Books.query.filter_by(user_id = 0).all()
    #available_books = Books.query.filter_by()
    #remaining time => 
    return render_template("books.html",books = books)


@app.route("/profile",methods = ['GET','POST'])
@login_required
def profile():
    user = User.query.filter_by(id = session["user_id"]).first()
    books = Books.query.filter_by(user_id = session["user_id"]).all()
    


    return render_template("profile.html",books = books )






@app.route('/register', methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        #hashed_password = bcrypt.generate_password_hash(password)
       
        user = User.query.filter_by(username=username).one_or_none()
        try:
            if user.username == username : 
                # route pages will come here
                return "this username is already used please come back and select another username"
        except:
            new_user = User(username=username,email=email,password=password,book_count = 0 , penalty = 0)
            db.session.add(new_user)
            db.session.commit()
            return "User added"
   
    return render_template("register.html")






@app.route('/rent_book',methods = ['GET','POST'])
def rent_book():
    
    if request.method == 'POST':
        user = User.query.filter_by(id = session["user_id"]).first()
        books = Books.query.filter_by(user_id = session["user_id"]).all()
        if user.book_count >= 3:
            return "Error"
        for i in range(0,len(books)):
            if diffrence_between_dates(books[i].last_rent_date,datetime.now()) < 0:
                flash('You must return your out-dated book first',"error")
                return redirect(url_for('profile'))
        # catch inputs from html
        book_id = request.form['book']
        date = request.form['date']
        # string date converting to datetime date
        date_converted = convert_date(date)

        #catch book from db where selected book_id from html
        book = Books.query.filter_by(id=book_id).first()
        # update book user_id
        book.user_id = session["user_id"]
        # update book rent_date 
        book.rent_date = datetime.now()
        book.last_rent_date = date_converted
        user.book_count += 1
        # db apply
        db.session.commit()
        return redirect(url_for("book_page"))
    return redirect(url_for("book_page"))
    

@app.route('/re_rent',methods = ['GET','POST'])
def re_rent_book():
    if request.method == 'POST':
        book_id = request.form['book']
        book = Books.query.filter_by(id=book_id).first()
        book.rent_date = None
        book.last_rent_date = None
        book.user_id = 0
        book.last_user = session['user_id']
        db.session.commit()
        return redirect(url_for("profile"))



def diffrence_between_dates(lastrent_date,rent_date):
    return ((lastrent_date-rent_date).days) + 1


def convert_date(d1):
    d1 = datetime.fromisoformat(d1)
    return d1