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