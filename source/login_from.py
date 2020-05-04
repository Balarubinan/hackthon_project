from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField,RadioField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField("Know me??")
    acc_type=RadioField('Account type',validators=[DataRequired()],choices=['Farmer','Retailer'])
    submit=SubmitField('Sign in')
