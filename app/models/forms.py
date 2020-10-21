from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf.form import Form
from wtforms import  TextField, TextAreaField, SubmitField, validators, ValidationError

class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    remember = BooleanField("remember")
 
class ResgisterForm(FlaskForm):
    username = StringField("username")
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    remember = BooleanField("remember")

class ContactForm(Form):
  name = TextField("Name",  [validators.Required("Please enter your name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
  message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
  submit = SubmitField("Send")