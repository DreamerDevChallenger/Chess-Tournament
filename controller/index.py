class PlayerController:
    def __init__(self, model, view):
        """Init PlayerController

        Args:
            model (func): return model
            view (func): return view
        """
        self.model = model
        self.view = view

    def add_player(self, player):
        """Add player

        Args:
            player (Object): player model
        """
        self.model.add_player(player)
        self.view.display_message(f"Player {player['firstname']} added successfully.")

    def show_players(self):
        """show all players"""
        players = self.model.get_players()
        self.view.display_players(players)


class TournamentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_tournament(self, tournament):
        """Add tournament

        Args:
            tournament (Object): player model
        """
        self.model.add_tournament(tournament)
        self.view.display_message(
            f"Tournament {tournament['name']} added successfully."
        )

    def show_tournaments(self):
        """show all tournaments"""
        tournaments = self.model.get_tournaments()
        self.view.display_tournaments(tournaments)

    def add_player_to_tournament(self, tournament_id, player_id):
        """Add tournament in tournamnet

        Args:
            tournament_id (string): tournament id
            player_id (string): player id
        """
        self.model.add_player_to_tournament(tournament_id, player_id)
        self.view.display_message(
            f"Player {player_id} added to tournament {tournament_id}."
        )

    def add_round_to_tournament(self, tournament_id, round_info):
        """Add round in tournamenr

        Args:
            tournament_id (string): tournamnet id
            round_info (string): round's description
        """
        self.model.add_round_to_tournament(tournament_id, round_info)
        self.view.display_message(
            f"Round {round_info['round_number']} added to tournament {tournament_id}."
        )
