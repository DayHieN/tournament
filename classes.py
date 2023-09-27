import random

# Exceptions


class MaxNumberException(Exception):
    pass


class NotSuchElement(Exception):
    pass

# Classes


class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_player_info(self):
        print(f" Player {self.name} - age {self.age}")


class Team:
    def __init__(self, name):
        self.max_players = 5
        self.name = name
        self.players = []

    def viable_addition(self, player):
        if len(self.players) < self.max_players:
            return
        else:
            raise MaxNumberException(
                f"\nCouldn't add {player.name} to {self.name}. Max number of players in the team is {self.max_players}."
            )

    def viable_removal(self, player):
        if player in self.players:
            return
        else:
            raise NotSuchElement(
                f"\nCouldn't remove {player}. No such player exists in {self.name}."
            )

    def add_players_to_team(self, player):
        try:
            self.viable_addition(player)
            self.players.append(player)
            print(f"\n{player.name} added to {self.name}.")
        except MaxNumberException as error:
            print(f"\nError: {error}")

    def remove_players_from_team(self, player):
        try:
            self.viable_removal(player)
            self.players.remove(player)
            print(f"\n{player.name} removed from team {self.name}.")
        except NotSuchElement as error:
            print(f"\nError: {error}")

    def show_team_info(self):

        print(f"\nTeam {self.name}")
        if len(self.players) > 0:
            print("Players:")
            for player in self.players:
                player.show_player_info()


class Tournament:
    def __init__(self, name, max_teams):
        self.max_teams = max_teams
        self.name = name
        self.teams = []

    def viable_addition(self, team):
        if len(self.teams) < self.max_teams:
            return
        else:
            raise MaxNumberException(
                f"Couldn't add {team.name} to {self.name}. Max number of teams in the tournament is {self.max_teams}."
            )

    def viable_removal(self, team):
        if team in self.teams:
            return
        else:
            raise NotSuchElement(
                f"\nCouldn't remove {team}. No such team exists in {self.name}."
            )

    def add_teams_to_tournament(self, team):
        try:
            self.viable_addition(team)
            self.teams.append(team)
            print(f"\n{team.name} added to {self.name}.")
        except MaxNumberException as error:
            print(f"\nError: {error}")

    def remove_teams_from_tournament(self, team):
        try:
            self.viable_removal(team)
            self.teams.remove(team)
            print(f"\n{team.name} removed from team {self.name}.")
        except NotSuchElement as error:
            print(f"\nError: {error}")

    def show_tournament_info(self):
        print(f"{self.name} - {self.max_teams} teams\nTeams:")
        for team in self.teams:
            print(f"{team.name}\n Players:{team.show_team_info()}")

    def create_matches(self):
        matches = []
        if len(self.teams) == self.max_teams:
            random.shuffle(self.teams)
            for i in range(0, len(self.teams), 2):
                if i+1 < len(self.teams):
                    match = (self.teams[i], self.teams[i+1])
                    matches.append(match)
        for match in matches:
            print(f"\n{match[0].name} vs {match[1].name}")
