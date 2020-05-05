from flask import Flask, render_template, flash, redirect, url_for, request
from source import login_from
from source.login_from import Form, SignUpForm, PostHarvestForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'raj'


@app.route('/About')
def about():
    return render_template('about.html')


@app.route('/history_farm')
def farmer_history():
    history = ['empty']  # testing puprose once Db added the function will be inserted
    return render_template('farmer_history_page.html', history_list=history)


@app.route('/history_sales')
def retailer_history():
    history = ['empty']  # testing purpose
    return render_template('retailer_history_page.html', history_list=history)


@app.route('/post_farmer', methods=['GET', 'POST'])
def postfarmer():
    postdet = PostHarvestForm()
    if postdet.postdescript.data != None:
        # add fucntion for savig post
        return redirect('/Farmer_page')
    return render_template('post_harvest.html', postdet=postdet)


@app.route('/post_retailer', methods=['GET', 'POST'])
def postretailer():
    postdet = PostHarvestForm()  # both the forms are similar in manner hence same class obeject used
    if postdet.postdescript.data != None:
        print(postdet.postdescript.data)  # add DB function for saveing post
        return redirect('/Retailer_page')
    return render_template('post_retailer.html', postdet=postdet)


@app.route('/Farmer_page')
def farmer_page():
    retailer_posts = ['post1', 'post2', 'post3']
    return render_template('farmer_page.html', retailer_posts=retailer_posts)


@app.route('/Retailer_page')
def retailer_page():
    return render_template('retailer_page.html')


@app.route('/Auction_page')
def auction_page():
    print("Visited")
    lis = ["Auction1", "Auction2", "Auction3"]  # use the data fetched from the db
    # as the input list here
    return render_template('auction_page.html', auction_list=lis)


@app.route('/home', methods=['GET', 'POST'])
def remain():
    form = Form()
    # access the database and get the needed authencation
    if form.username.data == "admin" and form.password.data == "admin":
        print('In here')
        return redirect(url_for(f'{form.acc_type.data.lower()}_page'))
    return render_template('main_page.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    form = Form()
    # access the database and get the needed authencation
    if form.username.data == "admin" and form.password.data == "admin":
        print('In here')
        return redirect(url_for(f'{form.acc_type.data.lower()}_page'))
    return render_template('main_page.html', form=form)


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
    form = SignUpForm()
    if form.username.data != None:
        # pass # insert db operations here
        # if accepted redirect to the root fmainpage.htmml
        return redirect('/home')
    return render_template('signup.html', title='SIGN UP', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
