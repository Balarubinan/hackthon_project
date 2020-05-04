from flask import Flask,render_template,flash,redirect,url_for,request
from source import login_from
from source.login_from import Form
app = Flask(__name__)
app.config['SECRET_KEY']='raj'

@app.route('/Farmer_page')
def farmer_page():
    return render_template('farmer_page.html')

@app.route('/signup')
def index():
    return render_template('signup.html')

@app.route('/home')
def remain():
    return render_template('main_page.html')

@app.route('/',methods=['GET','POST'])
def mainpage():
    form=Form()
    # access the database and get the needed authencation
    if form.username.data=="admin" and form.password.data=="admin":
        print('In here')
        return redirect(url_for(f'{form.acc_type.data.lower()}_page'))
    return render_template('main_page.html',form=form)

@app.route('/login',methods=['GET','POST'])
def log_on():
    form=Form()
    if form.validate_on_submit():
        # here iss where i should use my good old sqldatabase skills to store the damn files
        flash(f'Login requested for user {form.username.data} and {form.remember.data}')
        return redirect('/')
    return render_template('login_template.html',title='SIGN IN',form=form)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')