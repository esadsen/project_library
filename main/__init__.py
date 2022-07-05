import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

bcrypt = Bcrypt(app)






db = SQLAlchemy(app)
#here => db.config[]