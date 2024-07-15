class PlayerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_player(self, player):
        self.model.add_player(player)
        self.view.display_message(f"Player {player['username']} added successfully.")

    def show_players(self):
        players = self.model.get_players()
        self.view.display_players(players)

class RoundController:
    def __init__(self, model, view):
        self.model = model

class TournamentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_tournament(self, tournament):
        self.model.add_tournament(tournament)
        self.view.display_message(f"Tournament {tournament['name']} added successfully.")

    def show_tournaments(self):
        tournaments = self.model.get_tournaments()
        self.view.display_tournaments(tournaments)

    def add_player_to_tournament(self, tournament_id, player_id):
        self.model.add_player_to_tournament(tournament_id, player_id)
        self.view.display_message(f"Player {player_id} added to tournament {tournament_id}.")