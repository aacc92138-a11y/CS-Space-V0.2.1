from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,SubmitField,validators

class VipForm(FlaskForm):
    name = StringField("Name",validators=[validators.DataRequired()])
    email = EmailField("Email",validators=[validators.DataRequired()])
    password = PasswordField("Password",validators=[validators.DataRequired()])
    
