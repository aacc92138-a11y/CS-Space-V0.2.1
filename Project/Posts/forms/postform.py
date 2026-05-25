from wtforms import TextAreaField,FileField,SubmitField,validators
from flask_wtf import FlaskForm

class PostsForm(FlaskForm):
    txt = TextAreaField('اكتب ما يدور في بالك',validators=[validators.DataRequired()])
    file = FileField("Picture")
    submit = SubmitField("Submit")
