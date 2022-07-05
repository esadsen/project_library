
from flask_wtf import FlaskForm
from wtforms import StringField,TextField,PasswordField,ValidationError
from wtforms.validators import DataRequired,Email,InputRequired,Optional




class LoginForm(FlaskForm):
    username = TextField('Username',id='username_login',validators = [DataRequired()])
    password = PasswordField('Password',id='pwd_login',validators=[DataRequired()])    



class AddBook(FlaskForm):
    name=TextField("Book Name:",id="book_name",validators=[DataRequired()])
    isbn=TextField("Isbn Number:",id="isbn_number",validators=[DataRequired()])