from classes import *
import json

with open('players.json') as file:
    players = json.load(file)


teams = []

players_instances = [Player(player['name'], player['age'])
                     for player in players]



current_team = None
for player in players_instances:
    if current_team is None or len(current_team.players) == 5:
        team_name = f"Team{len(teams) + 1}"
        current_team = Team(team_name)
        teams.append(current_team)
    current_team.add_players_to_team(player)


pajaritos_tournament = Tournament('Pajaritos', 8)

for team in teams:
    pajaritos_tournament.add_teams_to_tournament(team)

pajaritos_tournament.create_matches()

