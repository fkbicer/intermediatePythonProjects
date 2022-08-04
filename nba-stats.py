from ast import Lambda
from requests import get, request
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

def get_scorebard():   
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:
        printer.pprint(game.keys())
        break

def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['preseason']['teams']

    print(teams[0])
    # teams = list(filter(lambda x: x['name'] != "Team", teams))

    for team in teams:
        teamId = team['teamId']
        nickname = team['nickname']
        name = team['name']
        abbreviation = team['abbreviation'] 
        print(f"{teamId} - {name} - {nickname}- {abbreviation} ")
    
get_stats()
