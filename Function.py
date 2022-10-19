import statsapi
import logging
AVG = .243

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

def compareToAverage(name1,name2,name3):
    p1Count = 0;
    p2Count = 0;
    p3Count = 0;
    p1 = getplayer(name1, "season", "hitting")
    p1_stat = float(getSepcificStatNum(p1, "avg"))
    p2 = getplayer(name2, "season", "hitting")
    p2_stat = float(getSepcificStatNum(p2, "avg"))
    p3 = getplayer(name3, "season", "hitting")
    p3_stat = float(getSepcificStatNum(p3, "avg"))
    differnce = abs(p1_stat - AVG)
    if (p1_stat > AVG):
        p1Count += (differnce * 100)
        print(name1 + " has " + str(p1Count) + " more than average")
    if(p2_stat > AVG):
        p1Count += (differnce * 100)
        print(name2 + " has " + str(p2Count) + " more than average")
    if (p3_stat > AVG):
        p3Count += (differnce * 100)
        print(name3 + " has " + str(p3Count) + " more than average")
    if(p1Count > p2Count and p1Count > p3Count):
        print(name1 + " is the best lead off ")
    if (p2Count > p1Count and p2Count > p1Count):
        print(name2 + " is the best lead off ")
    if(p3Count > p1Count and p3Count > p1Count):
        print(name3 + " is the best lead off ")
