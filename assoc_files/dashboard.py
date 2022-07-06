from flask_security import password_reset
from assoc_files.config import bcrypt
from assoc_files.config import app
from flask import Flask, flash, redirect,url_for, render_template, request , session
from assoc_files.model import User , Books
from assoc_files.config import db
from functools import wraps



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
                session["logged_in"] = True
                session["user_id"] = user.id
                return render_template("index.html")
        except:    
            return "auth failed"

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")


@app.route('/books')

def book_page():

    books = Books.query.filter_by(user_id=session['user_id']).all()
    #remaining time => 
    return render_template("books.html",books = books)


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
            new_user = User(username=username,email=email,password=password)
            db.session.add(new_user)
            db.session.commit()
            return "User added"
   
    return render_template("register.html")