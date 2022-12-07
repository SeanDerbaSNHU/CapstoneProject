# This file is used for setting up web pages, all addresses should be put here
from flask import Flask, render_template, Blueprint, redirect, url_for, request
from testing import getdata
import Function

from Function import createLinup, getplayerCareer



auth = Blueprint('auth', __name__)

pTemp = 'test'
pList = []

# use decorators to link the function to a url
@auth.route('/', methods=['GET', 'POST'])
def index():
    error = None
    # pList = []
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
            if(stats != None):
                fullname = stats['first_name'] + " " + stats['last_name']
                stats = stats['stats'][0]['stats']
                gamesPlayed = stats['gamesPlayed']
                batAvg = stats['avg']
                hr = stats['homeRuns']
                so = stats['strikeOuts']
                RBI = stats['rbi']
                global pTemp
                pTemp = fullname
            return render_template('index.html', error=error, name=fullname, gamesPlayed=gamesPlayed, batAvg=batAvg,
                                   homeruns=hr, strikeouts=so, rbi=RBI)
        else:
            return render_template('index.html', error=error)

    return render_template('index.html', error=error)  # return a string



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
            if(stats != None):
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




@auth.route('/sortedLineup')
def sortedLineup():
    #use sorting function to sort pList
    #Display sorted pList
    sList = createLinup(pList)
    return render_template('sortedLineup.html', p1 = sList[0], p2 = sList[1], p3 = sList[2], p4 = sList[3], p5 = sList[4], p6 = sList[5], p7 = sList[6], p8 = sList[7], p9 = sList[8])

