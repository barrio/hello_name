from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class UserForm(FlaskForm):
    email = StringField(
        'Email:', validators=[Email('Please enter a valid email address'), DataRequired()]
    )
    submit = SubmitField('Submit')
