from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from psrapp.models import User

REPORT_CATEGORIES =(
    ("1", "Accident"),
    ("2", "Traffic"),
    ("3", "Hazard")
)

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=10)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Control to avoid the registration with the same username or email address
    def validate_username(self, username):
        # Query the database
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ReportForm(FlaskForm):
    category= SelectField(label='Category', choices=REPORT_CATEGORIES)
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=50)])
    description = TextAreaField('Description', validators=[DataRequired() , Length(min=5, max=250)])
    attachment = FileField('Attachment')
    submit = SubmitField('Send')

