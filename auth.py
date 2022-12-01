# This file is used for setting up web pages, all addresses should be put here
from flask import Flask, render_template, Blueprint, redirect, url_for, request
from testing import getdata
from Function import createLinup, getplayerCareer


auth = Blueprint('auth', __name__)

pTemp = 'test'
pList = []

# use decorators to link the function to a url
@auth.route('/')
def index():
    pList = []
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
    pList = []
    return render_template('welcome.html')  # render a template


@auth.route('/login', methods=['GET', 'POST'])
def login():
    pList = []
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('/welcome')
    return render_template('login.html', error=error)


@auth.route('/register')
def register():
    pList = []
    from app import db
    return render_template('register.html')


@auth.route('/logout')
def logout():
    pList = []
    return 'Logout'


@auth.route('/profile')
def profile():
    pList = []
    return render_template('profile.html')





@auth.route('/lineup', methods=['GET', 'POST'])
def lineup():
    #players = createLinup(["Aaron Judge", "Anthony Rizzo", "Kyle Higashioka","Andrew Benintendi", "Aaron Hicks","Jose Trevino","Tim Locastro","Josh Donaldson", "Harrison Bader"])
    #return render_template('lineup.html', player1 = players[0], player2 = players[1], player3 = players[2], player4 = players[3], player5 = players[4], player6 = players[5], player7 = players[6], player8 = players[7], player9 = players[8])
    error = None
    #pList = []
    pName = ''
    fullname = ''
    gamesPlayed = ''
    batAvg = ''
    hr = ''
    so = ''
    RBI = ''

    if request.method == 'POST':
        if request.form['btn_identifier'] == 'search':
            pName = request.form['playerName']
            stats = getplayerCareer(pName)
            fullname = stats['first_name'] + " " + stats['last_name']
            stats = stats['stats'][0]['stats']
            gamesPlayed = stats['gamesPlayed']
            batAvg = stats['avg']
            hr = stats['homeRuns']
            so = stats['strikeOuts']
            RBI = stats['rbi']
            global pTemp
            pTemp = fullname
            return render_template('lineup.html', error = error, name = fullname, gamesPlayed = gamesPlayed, batAvg = batAvg, homeruns = hr, strikeouts = so, rbi = RBI)
        elif request.form['btn_identifier'] == 'add':
            #pName = request.form['playerName']
            #stats = getplayerCareer(pName)
            #fullname = stats['first_name'] + " " + stats['last_name']
            pList.append(pTemp)
            if len(pList) == 1:
                return render_template('lineup.html', error=error, name=fullname, gamesPlayed=gamesPlayed, batAvg=batAvg,
                                       homeruns=hr, strikeouts=so, rbi=RBI, p1 = pList[0])
            elif len(pList) == 2:
                return render_template('lineup.html', error=error, name=fullname, gamesPlayed=gamesPlayed, batAvg=batAvg,
                                       homeruns=hr, strikeouts=so, rbi=RBI, p1 = pList[0], p2 = pList[1])
            elif len(pList) == 3:
                return render_template('lineup.html', error=error, name=fullname, gamesPlayed=gamesPlayed, batAvg=batAvg,
                                       homeruns=hr, strikeouts=so, rbi=RBI, p1 = pList[0], p2 = pList[1], p3 = pList[2])
            elif len(pList) == 4:
                return render_template('lineup.html', error=error, name=fullname, gamesPlayed=gamesPlayed, batAvg=batAvg,
                                       homeruns=hr, strikeouts=so, rbi=RBI, p1 = pList[0], p2 = pList[1], p3 = pList[2], p4 = pList[3])
            elif len(pList) == 5:
                return render_template('lineup.html', error=error, name=fullname, gamesPlayed=gamesPlayed, batAvg=batAvg,
                                       homeruns=hr, strikeouts=so, rbi=RBI, p1 = pList[0], p2 = pList[1], p3 = pList[2], p4 = pList[3], p5 = pList[4])
            elif len(pList) == 6:
                return render_template('lineup.html', error=error, name=fullname, gamesPlayed=gamesPlayed, batAvg=batAvg,
                                       homeruns=hr, strikeouts=so, rbi=RBI, p1 = pList[0], p2 = pList[1], p3 = pList[2], p4 = pList[3], p5 = pList[4], p6 = pList[5])
            elif len(pList) == 7:
                return render_template('lineup.html', error=error, name=fullname, gamesPlayed=gamesPlayed, batAvg=batAvg,
                                       homeruns=hr, strikeouts=so, rbi=RBI, p1 = pList[0], p2 = pList[1], p3 = pList[2], p4 = pList[3], p5 = pList[4],
                                       p6 = pList[5], p7 = pList[6])
            elif len(pList) == 8:
                return render_template('lineup.html', error=error, name=fullname, gamesPlayed=gamesPlayed, batAvg=batAvg,
                                       homeruns=hr, strikeouts=so, rbi=RBI, p1 = pList[0], p2 = pList[1], p3 = pList[2], p4 = pList[3], p5 = pList[4],
                                       p6 = pList[5], p7 = pList[6], p8 = pList[7])
            elif len(pList) == 9:
                return render_template('lineup.html', error=error, name=fullname, gamesPlayed=gamesPlayed, batAvg=batAvg,
                                       homeruns=hr, strikeouts=so, rbi=RBI, p1 = pList[0], p2 = pList[1], p3 = pList[2], p4 = pList[3], p5 = pList[4],
                                       p6 = pList[5], p7 = pList[6], p8 = pList[7], p9 = pList[8])
        elif request.form['btn_identifier'] == 'submit':
            if (1):
                return redirect('/sortedLineup')
            else:
                #return error statement
                return render_template('lineup.html', error = error)
        else:
            return render_template('lineup.html', error = error)

    return render_template('lineup.html', error = error)


@auth.route('/standings')
def standings():
    pList = []
    return render_template('standings.html')

@auth.route('/sortedLineup')
def sortedLineup():
    #use sorting function to sort pList
    #Display sorted pList
    sList = createLinup(pList)
    return render_template('sortedLineup.html', p1 = sList[0], p2 = sList[1], p3 = sList[2], p4 = sList[3], p5 = sList[4], p6 = sList[5], p7 = sList[6], p8 = sList[7], p9 = sList[8])

