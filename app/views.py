from flask import render_template, flash, redirect, g, url_for, request
from flask.ext.login import login_user , logout_user , current_user , login_required, LoginManager
from app import app
from app.models import User, db
import vk

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    return render_template("index.html",
        title = 'Home',
        user = user)

# @app.route('/user/<user>')
# def show_user_profile(user):
#     return 'User %s' % user

@app.route('/login',methods=['GET','POST'])
def login():
    if g.user is not None and (g.user.is_authenticated ==True):
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(url_for('index'))

    # try:
    #     user = User.get(username)
    # except:
    #       user = None
    #
    # if user and user.check_password(password):
    #     login_user(user, force=True)
    #     return redirect(request.form['next'] or url_for("index"))
    # else:
    #     error = 'Username/Password incorrect.'
    #     return render_template('login.html',
    #             title='Sign In',
    #             error=error)
    #
    # return render_template('login.html',
    #     form=form,
    #     title='Sign In')



@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'], request.form['password'], request.form['email'])
    registered_user = User.query.filter_by(username=request.form['username'],password=request.form['password']).first()
    if user != registered_user:
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered')
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    logout_user()
    return redirect('/index')


