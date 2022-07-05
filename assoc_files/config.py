
from re import A
import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)

bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:fehmimustafa@database-server-instance-1.cp3fdruwvi5c.us-east-1.rds.amazonaws.com/db_server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




app.config['SECRET_KEY'] = 'fehmimustafa'

from assoc_files import dashboard