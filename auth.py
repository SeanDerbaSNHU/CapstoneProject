# This file is used for setting up web pages, all addresses should be put here
from flask import Flask, render_template, Blueprint, redirect, url_for, request
from testing import getdata
from app import db
import Function
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


@auth.route('/standings')

def standings():
    error = None
    num = 201
    stat_dict = Function.getStanding("103")
    if request.method == 'POST':
        num = 202
    stats = stat_dict[num]
    print(stats)
    team1 = stats['teams'][0]
    name1 = team1['name']
    w1 = team1['w']
    l1 = team1['l']
    p1 = round((team1['w']/(team1['w']+team1['l']))*100, 2)
    gb1 = team1['gb']
    team2 = stats['teams'][1]
    name2 = team2['name']
    w2 = team2['w']
    l2 = team2['l']
    p2 = round((team2['w'] / (team2['w'] + team2['l'])) * 100, 2)
    gb2 = team2['gb']
    team3 = stats['teams'][2]
    name3 = team3['name']
    w3 = team3['w']
    l3 = team3['l']
    p3 = round((team3['w'] / (team3['w'] + team3['l'])) * 100, 2)
    gb3 = team3['gb']
    team4 = stats['teams'][3]
    name4 = team4['name']
    w4 = team4['w']
    l4 = team4['l']
    p4 = round((team4['w'] / (team4['w'] + team4['l'])) * 100, 2)
    gb4 = team4['gb']
    team5 = stats['teams'][4]
    name5 = team5['name']
    w5 = team5['w']
    l5 = team5['l']
    p5 = round((team5['w'] / (team5['w'] + team5['l'])) * 100, 2)
    gb5 = team5['gb']
    return render_template('standings.html', data= "<h1> American League East </h1>", error = error, name1 = name1, w1 = w1, l1 = l1, p1 = p1, gb1 = gb1, name2 = name2, w2 = w2, l2 = l2, p2 = p2, gb2 = gb2, name3 = name3, w3 = w3, l3 = l3, p3 = p3, gb3 = gb3, name4 = name4, w4 = w4, l4 = l4, p4 = p4, gb4 = gb4,name5 = name5, w5 = w5, l5 = l5, p5 = p5, gb5 = gb5)


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