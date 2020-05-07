from flask import Flask, render_template, flash, redirect, url_for, request,g
# from source import login_from
from login_from import Form, SignUpForm, PostHarvestForm,User,Auction,AuctionForm
from databasefunctions import *
import sqlite3 as sq
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'raj'

cur_user=User()

DATABASE = '/home/Balarubinan/mysite/database.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sq.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()



# fuction to create an auction
@app.route('/create_auction',methods=['GET','POST'])
def create_auction():
    auct=AuctionForm() # Creating form to hold the auction details
    if auct.title.data!=None:
        auct_obj=Auction()
        auct_obj.st_by=auct.st_by
        auct_obj.title=auct.title.data
        auct_obj.content=auct.content.data
        auct_obj.date=datetime.now()
        auct_obj.id=random.randint(1,1000)
        auct_obj.cur_bid=auct.cur_bid.data
        auct_obj.bids=0
        auct_obj.last_bidder=cur_user.name
        #insert db write code here
        add_auction(auct_obj)
        return redirect('/Retailer_page')
    return render_template('create_auction.html',auct=auct)


@app.route('/About')
def about():
    return render_template('about.html')


@app.route('/history_farm')
def farmer_history():
    # history=fetch_his_posts(cur_user.name,'1')
    history=fetch_posts('1')
    return render_template('farmer_history_page.html', history_list=history)


@app.route('/history_sales')
def retailer_history():
    # history = ['empty']  # testing purpose
    # history=fetch_his_posts(cur_user.name,'2')
    history=fetch_posts('2')
    return render_template('retailer_history_page.html', history_list=history)


@app.route('/post_farmer', methods=['GET', 'POST'])
def postfarmer():
    postdet = PostHarvestForm()
    if postdet.postdescript.data != None:
        # add fucntion for savig post
        add_post(postdet.postname.data,postdet.postdescript.data,cur_user.name,'1')
        return redirect('/Farmer_page')
    return render_template('post_harvest.html',postdet=postdet)


@app.route('/post_retailer', methods=['GET', 'POST'])
def postretailer():
    postdet = PostHarvestForm()  # both the forms are similar in manner hence same class obeject used
    if postdet.postdescript.data != None:
        # print(postdet.postdescript.data)  # add DB function for saveing post
        add_post(postdet.postname.data,postdet.postdescript.data,cur_user.name,'2')
        return redirect('/Retailer_page')
    return render_template('post_retailer.html', postdet=postdet)


@app.route('/Farmer_page')
def farmer_page():
    retailer_posts = fetch_posts('2')
    return render_template('farmer_page.html', retailer_posts=retailer_posts)


@app.route('/Retailer_page')
def retailer_page():
    farmer_posts=fetch_posts('1')
    return render_template('retailer_page.html',farmer_posts=farmer_posts)


@app.route('/Auction_page')
def auction_page():
    print("Visited")
    # cur=get_db().cursor()
    lis = fetch_auctions() # use the data fetched from the db
    # as the input list here
    return render_template('auction_page.html', auction_list=lis)


@app.route('/home', methods=['GET', 'POST'])
def remain():
    form = Form()
    if form.username.data!=None:
        val=fetch_cred(form.username.data)[0]
        if val!=None and EncryptString(form.password.data)==val[4]:
            cur_user.initialize_values(form.username.data)
            if val[5]=='2':
                return redirect(url_for('retailer_page'))
            else:
                return redirect(url_for('farmer_page'))
    return render_template('main_page.html',form=form)


@app.route('/',methods=['GET', 'POST'])
def mainpage():
    form = Form()
    if form.username.data!=None:
        val=fetch_cred(form.username.data)[0]
        if val!=None and EncryptString(form.password.data)==val[4]:
            cur_user.initialize_values(form.username.data)
            if val[5]=='2':
                return redirect(url_for('retailer_page'))
            else:
                return redirect(url_for('farmer_page'))
    return render_template('main_page.html',form=form)


# The below route  wont be required as he maain page itself serves as a login page
# @app.route('/login',methods=['GET','POST'])
# def log_on():
#     form=Form()
#     if form.validate_on_submit():
#         flash(f'Login requested for user {form.username.data} and {form.remember.data}')
#         return redirect('/')
#     return render_template('login_template.html',title='SIGN IN',form=form)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    global cur_user
    form = SignUpForm()
    if form.username.data != None and form.password1.data==form.password2.data:
        cur_user.name=form.username.data
        cur_user.email=form.email.data
        cur_user.phone=form.phone.data
        cur_user.address=form.address.data
        cur_user.password=form.password1.data
        cur_user.type=form.acc_type.data
        # cursor=get_db().cursor()
        add_user(cur_user)
        # add_user(cur_user0
        return redirect('/home')
    return render_template('signup.html', title='SIGN UP', form=form)

@app.route('/debug')
def debug():
    lis=fetch_posts('1')
    return render_template('debug.html',list=lis)
# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1')

@app.route('/logout')
def logout():
    cur_user=None
    return redirect('/home')
