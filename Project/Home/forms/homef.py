from wtforms import StringField,validators,SubmitField,PasswordField,EmailField,BooleanField
from flask_wtf import FlaskForm

class SignUp(FlaskForm):
    Name = StringField("Username:",validators=[validators.DataRequired()])
    Email = EmailField("Email:",validators=[validators.Email(),validators.DataRequired()])
    Password = PasswordField("Password",validators=[validators.DataRequired()])
    Submit = SubmitField("Submit")

class SignIn(FlaskForm):
    Email = EmailField("Email:",validators=[validators.DataRequired(),validators.Email(),])
    Password = PasswordField("Password",validators=[validators.DataRequired()])
    rememberMe = BooleanField("Remember me")
    Submit = SubmitField("Submit")
