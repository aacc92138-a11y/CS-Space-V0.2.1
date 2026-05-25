from wtforms import TextAreaField,FileField,SubmitField,validators
from flask_wtf import FlaskForm

class Form(FlaskForm):
    user_input = TextAreaField(validators=[validators.DataRequired()])
    image = FileField()
    submit = SubmitField("نشر")