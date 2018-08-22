from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    email = StringField('Email:', validators=[Email('Please enter a valid email address'),
                                              DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=8)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')
