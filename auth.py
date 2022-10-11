from flask import Flask, render_template, Blueprint, redirect, url_for, request

auth = Blueprint('auth', __name__)


# use decorators to link the function to a url
@auth.route('/')
def home():
    return "Hello, World!"  # return a string

@auth.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('/welcome')
    return render_template('login.html', error=error)