from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,PasswordField,SubmitField,RadioField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from source.databasemod.databasefunctions import fetch_cred,fetch_auctions,fetch_auction

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
    address=StringField('Address',validators=[DataRequired()])
    phone=StringField('Phone',validators=[DataRequired()])
    email=EmailField('Email address',validators=[DataRequired()])
    acc_type = RadioField('Account type', validators=[DataRequired()], choices=['Farmer', 'Retailer'])
    submit = SubmitField('Sign up',render_kw={'type':"submit",'class':'signupbtn'})

class PostHarvestForm(FlaskForm):
    postname=StringField('Post Title:',validators=[DataRequired()])
    postdescript=StringField('Post Description',validators=[DataRequired()])
    submit = SubmitField('Post harvest details', render_kw={'type': "submit", 'class': 'signupbtn'})

# user defined class to
class User:
    def __init__(self):
        self.name=None
        self.password=None
        self.email=None
        self.phone=None
        self.address=None
        self.type=None
    def intialize_values(self,username):
        try:
            creds=fetch_cred(username)[0]
            self.name=username
            self.email=creds[1]
            self.phone=creds[2]
            self.address=creds[3]
            self.password=creds[4]
            self.type=creds[5]
        except Exception:
            return False

class Auction:
    def __init__(self):
        self.id=None
        self.title=None
        self.st_by=None
        self.cur_bid=None
        self.last_bidder=None
        self.bids=None
    def initialize_values(self,title):
        try:
            auct=fetch_auction(title)[0]
            self.id=auct[0]
            self.title=title
            self.st_by=auct[2]
            self.cur_bid=auct[3]
            self.last_bidder=auct[4]
            self.bids=auct[5]
        except Exception:
            return False




