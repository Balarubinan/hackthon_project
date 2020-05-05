from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField,RadioField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

# this class obejct is used to hold the sigin form for aldready exsting users
class Form(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField("Know me??")
    acc_type=RadioField('Account type',validators=[DataRequired()],choices=['Farmer','Retailer'])
    # we dont need this field as we can fetch the data from the
    submit=SubmitField('Sign in')

# this class is used to hold the Signup form
class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired()])
    remember = BooleanField("Know me??")
    email=EmailField('Email address',validators=[DataRequired()])
    acc_type = RadioField('Account type', validators=[DataRequired()], choices=['Farmer', 'Retailer'])
    submit = SubmitField('Sign up',render_kw={'type':"submit",'class':'signupbtn'})
