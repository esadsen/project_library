
from matplotlib.style import use
from assoc_files.config import bcrypt
from assoc_files.config import app
from flask import Flask,url_for, render_template, request
from assoc_files.model import User 
from assoc_files.config import db



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
        
        user = User.query.filter_by(username=username).first()
        if user.username == username and bcrypt.check_password_hash(user.password,password):
            return "auth success"
        else:
            return "auth failed"        
        
        

    return render_template("login.html")



@app.route('/register', methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        print(email,username,password,hashed_password)
        user = User.query.filter_by(username=username).one_or_none()
        try:
            if user.username == username : 
                # route pages will come here
                return "this username is already used please come back and select another username"
        except:
            new_user = User(username=username,email=email,password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return "User added"
        
            

        
        
    
    
    
    return render_template("register.html")