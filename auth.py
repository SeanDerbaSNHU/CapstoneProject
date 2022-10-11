# This file is used for setting up web pages, all addresses should be put here
from flask import Flask, render_template, Blueprint, redirect, url_for, request
from app import db

auth = Blueprint('auth', __name__)


# use decorators to link the function to a url
@auth.route('/')
def index():
    return render_template('index.html')  # return a string

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

@auth.route('/register')
def register():
    return render_template('register.html')

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/profile')
def profile():
    return render_template('profile.html')