# This file is used for setting up web pages, all addresses should be put here
from flask import Flask, render_template, Blueprint, redirect, url_for, request
from testing import getdata
from Function import createLinup


auth = Blueprint('auth', __name__)


# use decorators to link the function to a url
@auth.route('/')
def index():
    stat_dict = getdata()
    fullname = stat_dict['first_name'] + " " + stat_dict['last_name']
    stat_dict = stat_dict['stats'][0]['stats']
    gamesPlayed = stat_dict['gamesPlayed']
    batAvg = stat_dict['avg']
    hr = stat_dict['homeRuns']
    so = stat_dict['strikeOuts']
    RBI = stat_dict['rbi']
    return render_template('index.html', name = fullname, gamePlay = gamesPlayed, AVG = batAvg,homeRun = hr, SO =so, rbi = RBI)  # return a string


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
    from app import db
    return render_template('register.html')


@auth.route('/logout')
def logout():
    return 'Logout'


@auth.route('/profile')
def profile():
    return render_template('profile.html')


@auth.route('/lineup')
def lineup():
    players = createLinup(["Aaron Judge", "Anthony Rizzo", "Kyle Higashioka","Andrew Benintendi", "Aaron Hicks","Jose Trevino","Tim Locastro","Josh Donaldson", "Harrison Bader"])
    return render_template('lineup.html', player1 = players[0], player2 = players[1], player3 = players[2], player4 = players[3], player5 = players[4], player6 = players[5], player7 = players[6], player8 = players[7], player9 = players[8])