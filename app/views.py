from flask import render_template, flash, redirect
from app import app
@app.route('/')


@app.route('/index')
def index():
    user = { 'nickname': 'Tolya' } # выдуманный пользователь
    recipes = [ # список выдуманных постов
         {
                'title': { 'name': 'Cake' },
                'body': 'lalalala!'
        },
        {
                'title': { 'name': 'Cookies' },
                'body': 'some text!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        recipes = recipes)

@app.route('/user/<user>')
def show_user_profile(user):
    return 'User %s' % user

@app.route('/login')
def login():
    return render_template('login.html',
        title = 'Sign In',
 )