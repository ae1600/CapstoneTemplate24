# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired, NumberRange
from wtforms.fields.html5 import URLField, DateField, IntegerRangeField, EmailField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, RadioField
from wtforms_components import TimeField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role',choices=[("Teacher","Teacher"),("Student","Student")])



class ConsentForm(FlaskForm):
    adult_fname = StringField('First Name',validators=[DataRequired()])
    adult_lname = StringField('Last Name',validators=[DataRequired()])
    adult_email = EmailField('Email',validators=[Email()])
    consent = RadioField('Do you want your parents or teachers to see your sleep data/graph', choices=[(True,"True"),(False,"False")])
    submit = SubmitField('Submit')

class SleepForm(FlaskForm):
    starttime = TimeField("What Time Did You SLeep?")   
    endtime = TimeField("What Time Did You Wake Up?")   
    goal = TimeField("What was your goal wake up time?")
    sleep_date = DateField("What date did you go to sleep")
    wake_date = DateField("What date did you wake up")
    submit = SubmitField("Submit")

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Post!')

class DogForm(FlaskForm):
    name = StringField("Whats the dog's name?", validators=[DataRequired()])
    age = IntegerField("How old is the dog?", validators=[NumberRange(min=0,max=16, message="Enter a number between 0 and 16.")])
    likes = StringField('What are the likes and dislikes', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ClinicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    streetAddress = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zipcode',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')