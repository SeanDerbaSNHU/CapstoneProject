import statsapi
import logging
##League year by year averages for 30 plate apperances(also the average)

##first spot should ingore power hitters if they average more than .09 hr per game (more than 15 a season)
AVG = .243
SB = 0.51
HR = 6.601
RBI = 4.09
BB = 3.09


def getplayer(name, yearlyOrCareer, pos):
    #stat = statsapi.player_stats(next(x['id'] for x in statsapi.get('sports_players', {'season': 2022, 'gameType': 'W'})['people'] if x['fullName'] == name), pos, yearlyOrCareer)
    stat = statsapi.player_stat_data(next(x['id'] for x in statsapi.get('sports_players', {'season': 2022, 'gameType': 'W'})['people'] if x['fullName'] == name), pos, yearlyOrCareer, sportId=1)
    #stat = stat.split()[7:];
    return stat;

def getSepcificStat(stats, statName):
    index = 0
    stats_dict = {}

    while index < len(stats):
        stats_dict[stats[index]] = stats[index + 1]
        index += 2
    print(stats_dict.keys())
    final = statName + " :" + stats_dict[statName + ':']
    return final
def getSepcificStatNum(stats, statName):
    stats
    fullname = stats['first_name'] + " " + stats['last_name']
    stats = stats['stats'][0]['stats']
    final = stats[statName]
    return final

def compare(name1, name2, statName):
    p1 = getplayer(name1,"career", "hitting")
    p2 = getplayer(name2,"career", "hitting")
    p1_stat = getSepcificStatNum(p1,statName)
    p2_stat = getSepcificStatNum(p2,statName)
    differnce = abs(int(p1_stat) - int(p2_stat))
    if(p1_stat > p2_stat):
        print(name1 + " has " + str(differnce) + " more " + statName +" than " + name2)
    elif(p1_stat < p2_stat):
        print(name2 + " has " + str(differnce) + " more " + statName + " than " + name1)


def compareToAverage(testing):
    p1Count = 0
    p2Count = 0
    p3Count = 0
    editedList = [None] * 8
    output = [editedList,"string"]
    p1 = getplayer(testing[0], "season", "hitting")
    p1_stat = float(getSepcificStatNum(p1, "avg"))
    p2 = getplayer(testing[1], "season", "hitting")
    p2_stat = float(getSepcificStatNum(p2, "avg"))
    p3 = getplayer(testing[2], "season", "hitting")
    p3_stat = float(getSepcificStatNum(p3, "avg"))
    differnce1 = p1_stat - AVG
    differnce2 = p2_stat - AVG
    differnce3 = p3_stat - AVG
    p1_stat = float(getSepcificStatNum(p1, "baseOnBalls"))
    p2_stat = float(getSepcificStatNum(p2, "baseOnBalls"))
    p3_stat = float(getSepcificStatNum(p3, "baseOnBalls"))
    differnce1 = differnce1 + (p1_stat - BB)
    differnce2 += differnce2 + (p2_stat - BB)
    differnce3 +=  differnce3 + (p3_stat - BB)
    p1_stat = float(getSepcificStatNum(p1, "stolenBases"))
    p2_stat = float(getSepcificStatNum(p2, "stolenBases"))
    p3_stat = float(getSepcificStatNum(p3, "stolenBases"))
    differnce1 = differnce1 + (p1_stat - SB)*2
    differnce2 = differnce2 + (p2_stat - SB)*2
    differnce3 = differnce3 + (p3_stat - SB)*2
    p1_stat = float(getSepcificStatNum(p1, "caughtStealing"))
    p2_stat = float(getSepcificStatNum(p2, "caughtStealing"))
    p3_stat = float(getSepcificStatNum(p3, "caughtStealing"))
    differnce1 = differnce1 - p1_stat
    differnce2 = differnce2 - p2_stat
    differnce3 = differnce3 - p3_stat
    p1Count += (differnce1)
    p2Count += (differnce2)
    p3Count += (differnce3)
    playerDiffList = [p1Count,p2Count,p3Count]
    biggest = max(playerDiffList)
    first = playerDiffList.index(biggest)
    firstPerson = testing[first]
    print(str(p1Count) + " " + str(p2Count) + " " + str(p3Count))
    i = 0
    j = 0
    for x in range(9):
        if(testing[i] == firstPerson):
            i = i + 1
        else:
            editedList[j] = testing[i]
            i = i + 1
            j = j + 1
        print(i)
    output[0] = editedList
    print(editedList)
    output[1] = firstPerson
    return output

def second(input):
    p1Count = 0
    p2Count = 0
    p3Count = 0
    editedList = [None] * 7
    output = [editedList,"string"]
    print(input)
    p1 = getplayer(input[0], "season", "hitting")
    p1_stat = float(getSepcificStatNum(p1, "avg"))
    p2 = getplayer(input[1], "season", "hitting")
    p2_stat = float(getSepcificStatNum(p2, "avg"))
    p3 = getplayer(input[2], "season", "hitting")
    p3_stat = float(getSepcificStatNum(p3, "avg"))
    differnce1 = p1_stat - AVG
    differnce2 = p2_stat - AVG
    differnce3 = p3_stat - AVG
    p1_stat = float(getSepcificStatNum(p1, "baseOnBalls"))
    p2_stat = float(getSepcificStatNum(p2, "baseOnBalls"))
    p3_stat = float(getSepcificStatNum(p3, "baseOnBalls"))
    differnce1 = differnce1 + (p1_stat - BB)
    differnce2 += differnce2 + (p2_stat - BB)
    differnce3 += differnce3 + (p3_stat - BB)
    p1Count += (differnce1)
    p2Count += (differnce2)
    p3Count += (differnce3)
    playerDiffList = [p1Count, p2Count, p3Count]
    biggest = max(playerDiffList)
    first = playerDiffList.index(biggest)
    firstPerson = input[first]
    print(str(p1Count) + " " + str(p2Count) + " " + str(p3Count))
    i = 0
    j = 0
    for x in range(8):
        if (input[i] == firstPerson):
            i = i + 1
        else:
            editedList[j] = input[i]
            i = i + 1
            j = j + 1
        print(i)
    output[0] = editedList
    output[1] = firstPerson

    return output


def third(input):
    p1Count = 0
    p2Count = 0
    p3Count = 0
    editedList = [None] * 6
    output = [editedList,"string"]
    p1 = getplayer(input[0], "season", "hitting")
    p1_stat = float(getSepcificStatNum(p1, "avg"))
    p2 = getplayer(input[1], "season", "hitting")
    p2_stat = float(getSepcificStatNum(p2, "avg"))
    p3 = getplayer(input[2], "season", "hitting")
    p3_stat = float(getSepcificStatNum(p3, "avg"))
    differnce1 = p1_stat - AVG
    differnce2 = p2_stat - AVG
    differnce3 = p3_stat - AVG
    p1_stat = float(getSepcificStatNum(p1, "baseOnBalls"))
    p2_stat = float(getSepcificStatNum(p2, "baseOnBalls"))
    p3_stat = float(getSepcificStatNum(p3, "baseOnBalls"))
    differnce1 = differnce1 + (p1_stat - BB)
    differnce2 += differnce2 + (p2_stat - BB)
    differnce3 += differnce3 + (p3_stat - BB)
    p1_stat = float(getSepcificStatNum(p1, "homeRuns"))
    p2_stat = float(getSepcificStatNum(p2, "homeRuns"))
    p3_stat = float(getSepcificStatNum(p3, "homeRuns"))
    differnce1 = differnce1 + (p1_stat * 3)
    differnce2 += differnce2 + (p2_stat * 3)
    differnce3 += differnce3 + (p3_stat * 3)
    p1_stat = float(getSepcificStatNum(p1, "rbi"))
    p2_stat = float(getSepcificStatNum(p2, "rbi"))
    p3_stat = float(getSepcificStatNum(p3, "rbi"))
    differnce1 = differnce1 + (p1_stat - RBI)
    differnce2 += differnce2 + (p2_stat - RBI)
    differnce3 += differnce3 + (p3_stat - RBI)
    p1Count += (differnce1)
    p2Count += (differnce2)
    p3Count += (differnce3)
    playerDiffList = [p1Count, p2Count, p3Count]
    biggest = max(playerDiffList)
    first = playerDiffList.index(biggest)
    firstPerson = input[first]
    print(str(p1Count) + " " + str(p2Count) + " " + str(p3Count))
    i = 0
    j = 0
    for x in range(7):
        if (input[i] == firstPerson):
            i = i + 1
        else:
            editedList[j] = input[i]
            i = i + 1
            j = j + 1
        print(i)
    output[0] = editedList
    output[1] = firstPerson
    return output

def fourth(input):
    p1Count = 0
    p2Count = 0
    p3Count = 0
    editedList = [None] * 5
    output = [editedList,"string"]
    p1 = getplayer(input[0], "season", "hitting")
    p1_stat = float(getSepcificStatNum(p1, "avg"))
    p2 = getplayer(input[1], "season", "hitting")
    p2_stat = float(getSepcificStatNum(p2, "avg"))
    p3 = getplayer(input[2], "season", "hitting")
    p3_stat = float(getSepcificStatNum(p3, "avg"))
    differnce1 = p1_stat - AVG
    differnce2 = p2_stat - AVG
    differnce3 = p3_stat - AVG
    p1_stat = float(getSepcificStatNum(p1, "baseOnBalls"))
    p2_stat = float(getSepcificStatNum(p2, "baseOnBalls"))
    p3_stat = float(getSepcificStatNum(p3, "baseOnBalls"))
    differnce1 = differnce1 + (p1_stat - BB)
    differnce2 += differnce2 + (p2_stat - BB)
    differnce3 += differnce3 + (p3_stat - BB)
    p1_stat = float(getSepcificStatNum(p1, "homeRuns"))
    p2_stat = float(getSepcificStatNum(p2, "homeRuns"))
    p3_stat = float(getSepcificStatNum(p3, "homeRuns"))
    differnce1 = differnce1 + ((p1_stat - HR)*3)
    differnce2 += differnce2 + ((p2_stat - HR)*3)
    differnce3 += differnce3 + ((p3_stat - HR)*3)
    p1_stat = float(getSepcificStatNum(p1, "rbi"))
    p2_stat = float(getSepcificStatNum(p2, "rbi"))
    p3_stat = float(getSepcificStatNum(p3, "rbi"))
    differnce1 = differnce1 + (p1_stat - RBI)
    differnce2 += differnce2 + (p2_stat - RBI)
    differnce3 += differnce3 + (p3_stat - RBI)
    p1Count += (differnce1)
    p2Count += (differnce2)
    p3Count += (differnce3)
    playerDiffList = [p1Count, p2Count, p3Count]
    biggest = max(playerDiffList)
    first = playerDiffList.index(biggest)
    firstPerson = input[first]
    print(str(p1Count) + " " + str(p2Count) + " " + str(p3Count))
    i = 0
    j = 0
    for x in range(6):
        if (input[i] == firstPerson):
            i = i + 1
        else:
            editedList[j] = input[i]
            i = i + 1
            j = j + 1
        print(i)
    output[0] = editedList
    output[1] = firstPerson
    return output

def fith(input):
    p1Count = 0
    p2Count = 0
    p3Count = 0
    editedList = [None] * 4
    output = [editedList,"string"]
    p1 = getplayer(input[0], "season", "hitting")
    p1_stat = float(getSepcificStatNum(p1, "avg"))
    p2 = getplayer(input[1], "season", "hitting")
    p2_stat = float(getSepcificStatNum(p2, "avg"))
    p3 = getplayer(input[2], "season", "hitting")
    p3_stat = float(getSepcificStatNum(p3, "avg"))
    differnce1 = p1_stat - AVG
    differnce2 = p2_stat - AVG
    differnce3 = p3_stat - AVG
    p1_stat = float(getSepcificStatNum(p1, "baseOnBalls"))
    p2_stat = float(getSepcificStatNum(p2, "baseOnBalls"))
    p3_stat = float(getSepcificStatNum(p3, "baseOnBalls"))
    differnce1 = differnce1 + (p1_stat - BB)
    differnce2 += differnce2 + (p2_stat - BB)
    differnce3 += differnce3 + (p3_stat - BB)
    p1_stat = float(getSepcificStatNum(p1, "homeRuns"))
    p2_stat = float(getSepcificStatNum(p2, "homeRuns"))
    p3_stat = float(getSepcificStatNum(p3, "homeRuns"))
    differnce1 = differnce1 + (p1_stat * 3)
    differnce2 += differnce2 + (p2_stat * 3)
    differnce3 += differnce3 + (p3_stat * 3)
    p1_stat = float(getSepcificStatNum(p1, "rbi"))
    p2_stat = float(getSepcificStatNum(p2, "rbi"))
    p3_stat = float(getSepcificStatNum(p3, "rbi"))
    differnce1 = differnce1 + (p1_stat - RBI)
    differnce2 += differnce2 + (p2_stat - RBI)
    differnce3 += differnce3 + (p3_stat - RBI)
    p1Count += (differnce1)
    p2Count += (differnce2)
    p3Count += (differnce3)
    playerDiffList = [p1Count, p2Count, p3Count]
    biggest = max(playerDiffList)
    first = playerDiffList.index(biggest)
    firstPerson = input[first]
    print(str(p1Count) + " " + str(p2Count) + " " + str(p3Count))
    i = 0
    j = 0
    for x in range(5):
        if (input[i] == firstPerson):
            i = i + 1
        else:
            editedList[j] = input[i]
            i = i + 1
            j = j + 1
        print(i)
    output[0] = editedList
    output[1] = firstPerson
    return output

def six(input):
    p1Count = 0
    p2Count = 0
    p3Count = 0
    editedList = [None] * 3
    output = [editedList,"string"]
    p1 = getplayer(input[0], "season", "hitting")
    p1_stat = float(getSepcificStatNum(p1, "avg"))
    p2 = getplayer(input[1], "season", "hitting")
    p2_stat = float(getSepcificStatNum(p2, "avg"))
    p3 = getplayer(input[2], "season", "hitting")
    p3_stat = float(getSepcificStatNum(p3, "avg"))
    differnce1 = p1_stat - AVG
    differnce2 = p2_stat - AVG
    differnce3 = p3_stat - AVG
    p1_stat = float(getSepcificStatNum(p1, "baseOnBalls"))
    p2_stat = float(getSepcificStatNum(p2, "baseOnBalls"))
    p3_stat = float(getSepcificStatNum(p3, "baseOnBalls"))
    differnce1 = differnce1 + (p1_stat - BB)
    differnce2 += differnce2 + (p2_stat - BB)
    differnce3 += differnce3 + (p3_stat - BB)
    p1_stat = float(getSepcificStatNum(p1, "homeRuns"))
    p2_stat = float(getSepcificStatNum(p2, "homeRuns"))
    p3_stat = float(getSepcificStatNum(p3, "homeRuns"))
    differnce1 = differnce1 + (p1_stat - HR)
    differnce2 += differnce2 + (p2_stat - HR)
    differnce3 += differnce3 + (p3_stat - HR)
    p1_stat = float(getSepcificStatNum(p1, "rbi"))
    p2_stat = float(getSepcificStatNum(p2, "rbi"))
    p3_stat = float(getSepcificStatNum(p3, "rbi"))
    differnce1 = differnce1 + (p1_stat - RBI)
    differnce2 += differnce2 + (p2_stat - RBI)
    differnce3 += differnce3 + (p3_stat - RBI)
    p1Count += (differnce1)
    p2Count += (differnce2)
    p3Count += (differnce3)
    playerDiffList = [p1Count, p2Count, p3Count]
    biggest = max(playerDiffList)
    first = playerDiffList.index(biggest)
    firstPerson = input[first]
    print(str(p1Count) + " " + str(p2Count) + " " + str(p3Count))
    i = 0
    j = 0
    for x in range(4):
        if (input[i] == firstPerson):
            i = i + 1
        else:
            editedList[j] = input[i]
            i = i + 1
            j = j + 1
        print(i)
    output[0] = editedList
    output[1] = firstPerson
    return output

def seven(input):
    p1Count = 0
    p2Count = 0
    p3Count = 0
    editedList = [None] * 2
    output = [editedList,"string"]
    p1 = getplayer(input[0], "season", "hitting")
    p1_stat = float(getSepcificStatNum(p1, "avg"))
    p2 = getplayer(input[1], "season", "hitting")
    p2_stat = float(getSepcificStatNum(p2, "avg"))
    p3 = getplayer(input[2], "season", "hitting")
    p3_stat = float(getSepcificStatNum(p3, "avg"))
    differnce1 = p1_stat - AVG
    differnce2 = p2_stat - AVG
    differnce3 = p3_stat - AVG
    p1_stat = float(getSepcificStatNum(p1, "baseOnBalls"))
    p2_stat = float(getSepcificStatNum(p2, "baseOnBalls"))
    p3_stat = float(getSepcificStatNum(p3, "baseOnBalls"))
    differnce1 = differnce1 + (p1_stat - BB)
    differnce2 += differnce2 + (p2_stat - BB)
    differnce3 += differnce3 + (p3_stat - BB)
    p1_stat = float(getSepcificStatNum(p1, "homeRuns"))
    p2_stat = float(getSepcificStatNum(p2, "homeRuns"))
    p3_stat = float(getSepcificStatNum(p3, "homeRuns"))
    differnce1 = differnce1 + (p1_stat - HR)
    differnce2 += differnce2 + (p2_stat - HR)
    differnce3 += differnce3 + (p3_stat - HR)
    p1_stat = float(getSepcificStatNum(p1, "rbi"))
    p2_stat = float(getSepcificStatNum(p2, "rbi"))
    p3_stat = float(getSepcificStatNum(p3, "rbi"))
    differnce1 = differnce1 + (p1_stat - RBI)
    differnce2 += differnce2 + (p2_stat - RBI)
    differnce3 += differnce3 + (p3_stat - RBI)
    p1Count += (differnce1)
    p2Count += (differnce2)
    p3Count += (differnce3)
    playerDiffList = [p1Count, p2Count, p3Count]
    biggest = max(playerDiffList)
    first = playerDiffList.index(biggest)
    firstPerson = input[first]
    print(str(p1Count) + " " + str(p2Count) + " " + str(p3Count))
    i = 0
    j = 0
    for x in range(3):
        if (input[i] == firstPerson):
            i = i + 1
        else:
            editedList[j] = input[i]
            i = i + 1
            j = j + 1
        print(i)
    output[0] = editedList
    output[1] = firstPerson
    return output

def eight(input):
    p1Count = 0
    p2Count = 0
    p3Count = 0
    editedList = [None] * 1
    output = [editedList,"string"]
    p1 = getplayer(input[0], "season", "hitting")
    p1_stat = float(getSepcificStatNum(p1, "avg"))
    p2 = getplayer(input[1], "season", "hitting")
    p2_stat = float(getSepcificStatNum(p2, "avg"))
##    p3 = getplayer(input[2], "season", "hitting")
  ##  p3_stat = float(getSepcificStatNum(p3, "avg"))
    differnce1 = p1_stat - AVG
    differnce2 = p2_stat - AVG
    ##differnce3 = p3_stat - AVG
    p1_stat = float(getSepcificStatNum(p1, "baseOnBalls"))
    p2_stat = float(getSepcificStatNum(p2, "baseOnBalls"))
    ##p3_stat = float(getSepcificStatNum(p3, "baseOnBalls"))
    differnce1 = differnce1 + (p1_stat - BB)
    differnce2 += differnce2 + (p2_stat - BB)
   ## differnce3 += differnce3 + (p3_stat - BB)
    p1_stat = float(getSepcificStatNum(p1, "homeRuns"))
    p2_stat = float(getSepcificStatNum(p2, "homeRuns"))
   ## p3_stat = float(getSepcificStatNum(p3, "homeRuns"))
    differnce1 = differnce1 + (p1_stat - HR)
    differnce2 += differnce2 + (p2_stat - HR)
   ## differnce3 += differnce3 + (p3_stat - HR)
    p1_stat = float(getSepcificStatNum(p1, "rbi"))
    p2_stat = float(getSepcificStatNum(p2, "rbi"))
  ## p3_stat = float(getSepcificStatNum(p3, "rbi"))
    differnce1 = differnce1 + (p1_stat - RBI)
    differnce2 += differnce2 + (p2_stat - RBI)
   ## differnce3 += differnce3 + (p3_stat - RBI)
    p1Count += (differnce1)
    p2Count += (differnce2)
  ##  p3Count += (differnce3)
    playerDiffList = [p1Count, p2Count]
    biggest = max(playerDiffList)
    first = playerDiffList.index(biggest)
    firstPerson = input[first]
    ##print(str(p1Count) + " " + str(p2Count) + " " + str(p3Count))
    i = 0
    j = 0
    for x in range(2):
        if (input[i] == firstPerson):
            i = i + 1
        else:
            editedList[j] = input[i]
            i = i + 1
            j = j + 1
        print(i)
    output[0] = editedList
    output[1] = firstPerson
    return output

def nine(input):
    p1Count = 0
    p2Count = 0
    p3Count = 0
    editedList = [None]
    output = [editedList,"string"]
    p1 = getplayer(input[0], "season", "hitting")
    p1_stat = float(getSepcificStatNum(p1, "avg"))
    ##p2 = getplayer(input[1], "season", "hitting")
   ## p2_stat = float(getSepcificStatNum(p2, "avg"))
   ## p3 = getplayer(input[2], "season", "hitting")
   ## p3_stat = float(getSepcificStatNum(p3, "avg"))
    differnce1 = p1_stat - AVG
   ## differnce2 = p2_stat - AVG
   ## differnce3 = p3_stat - AVG
    p1_stat = float(getSepcificStatNum(p1, "baseOnBalls"))
   ## p2_stat = float(getSepcificStatNum(p2, "baseOnBalls"))
   ## p3_stat = float(getSepcificStatNum(p3, "baseOnBalls"))
    differnce1 = differnce1 + (p1_stat - BB)
    ##differnce2 += differnce2 + (p2_stat - BB)
    ##differnce3 += differnce3 + (p3_stat - BB)
    p1_stat = float(getSepcificStatNum(p1, "homeRuns"))
    ##p2_stat = float(getSepcificStatNum(p2, "homeRuns"))
    ##p3_stat = float(getSepcificStatNum(p3, "homeRuns"))
    differnce1 = differnce1 + (p1_stat - HR)
    ##differnce2 += differnce2 + (p2_stat - HR)
   ## differnce3 += differnce3 + (p3_stat - HR)
    p1_stat = float(getSepcificStatNum(p1, "rbi"))
   ## p2_stat = float(getSepcificStatNum(p2, "rbi"))
   ## p3_stat = float(getSepcificStatNum(p3, "rbi"))
    differnce1 = differnce1 + (p1_stat - RBI)
    ##differnce2 += differnce2 + (p2_stat - RBI)
   ##differnce3 += differnce3 + (p3_stat - RBI)
    p1Count += (differnce1)
    ##p2Count += (differnce2)
    ##p3Count += (differnce3)
    playerDiffList = [p1Count, p2Count, p3Count]
    biggest = max(playerDiffList)
    first = playerDiffList.index(biggest)
    print(input)
    firstPerson = input[0]
   ## print(str(p1Count) + " " + str(p2Count) + " " + str(p3Count))
    i = 0
    j = 0
    for x in range(1):
        if (input[i] == firstPerson):
            i = i + 1
        else:
            editedList[j] = input[i]
            i = i + 1
            j = j + 1
        print(i)
    output[0] = editedList
    output[1] = firstPerson
    return output
def createLinup(playerList):
    lineup = ["1", "1", "1","1","1","1","1","1","1"]
    holder = compareToAverage(playerList)
    playerList = holder[0]
    lineup[0] = holder[1]
    holder = second(playerList)
    playerList = holder[0]
    lineup[1] = holder[1]
    holder = third(playerList)
    playerList = holder[0]
    lineup[2] = holder[1]
    holder = fourth(playerList)
    playerList = holder[0]
    lineup[3] = holder[1]
    holder = fith(playerList)
    playerList = holder[0]
    lineup[4] = holder[1]
    holder = six(playerList)
    playerList = holder[0]
    lineup[5] = holder[1]
    holder = seven(playerList)
    playerList = holder[0]
    lineup[6] = holder[1]
    holder = eight(playerList)
    playerList = holder[0]
    lineup[7] = holder[1]
    holder = nine(playerList)
    playerList = holder[0]
    lineup[8] = holder[1]
    print(lineup)
    return lineup