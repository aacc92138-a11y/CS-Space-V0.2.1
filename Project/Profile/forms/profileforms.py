from wtforms import StringField,TextAreaField,SubmitField,validators
from flask_wtf import FlaskForm

class Bio(FlaskForm):
    bio=TextAreaField("Bio...")
    submit = SubmitField("حفظ")

class Info(FlaskForm):
    fname= StringField("الاسم الأول")
    lname = StringField("الاسم الأخير")
    submit = SubmitField("حفظ")