from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age')
    phone_number = StringField('Phone Number', validators=[DataRequired()])

class SearchContactsForm(FlaskForm):
    phone_number = StringField('Phone Number', validators=[DataRequired()])


