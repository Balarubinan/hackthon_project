from flask import Flask,render_template,flash,redirect
from source import login_from
from source.login_from import Form
app = Flask(__name__)
app.config['SECRET_KEY']='raj'

@app.route('/practice')
def index():
    return render_template('avengers.html')

@app.route('/thor')
def cakes():
    return render_template('Thor.html')

@app.route('/')
def func():
    user={'username':'Bala'}
    posts=[

        {'auth':'rubinan','says':'I dont care about shit'},
        {'auth':'raman','says':'This story is awesome'},
        {'auth':'Tasha','says':'This story is is the worst shit i have ever read in my whole life'},
    ]
    return render_template('demo.html',user=user,head_var="Just kiddind",posts=posts)

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