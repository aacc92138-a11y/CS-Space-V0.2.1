from wtforms import StringField,validators,SubmitField,PasswordField,EmailField,BooleanField
from flask_wtf import FlaskForm

class SignIn(FlaskForm):
    Email = EmailField("Email:",validators=[validators.DataRequired(),validators.Email(),])
    Password = PasswordField("Password",validators=[validators.DataRequired()])
    rememberMe = BooleanField("Remember me")
    Submit = SubmitField("Submit")
