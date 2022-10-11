import statsapi
import logging
import Function
logger = logging.getLogger('statsapi')
logger.setLevel(logging.DEBUG)
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)8s - %(name)s(%(thread)s) - %(message)s")
ch.setFormatter(formatter)
rootLogger.addHandler(ch)
print(statsapi.standings(leagueId=104,date='10/1/2022') )
print(statsapi.standings(leagueId=103, date='10/1/2022'))
print ("type name of player")
name = input()
print("type career or season")
careerOrSeason =input()
print("type hitting or pitching")
pos = input()

stats = Function.getplayer(name, careerOrSeason, pos)
for team in statsapi.lookup_team('ny'):
    print(team)
print("What stat")
statName = input()
final = Function.getSepcificStat(stats, statName)
print(final)

