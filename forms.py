from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    email = StringField(validators=[Email()])
    password = PasswordField(validators=[Length(min=8)])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField(validators=[Email()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField("Login")

class ProjectForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    description = TextAreaField(validators=[DataRequired()])
    submit = SubmitField("Add Project")

class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[Email()])
    message = TextAreaField(validators=[DataRequired()])
    submit = SubmitField("Send Message")
