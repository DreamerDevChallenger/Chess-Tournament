from model.index import PlayerModel, TournamentModel
from view.index import PlayerView
from controller.index import PlayerController, TournamentController


def main():
    player_model = PlayerModel()
    tournament_model = TournamentModel()
    player_controller = PlayerController(player_model, None)  # Initialize controller without view for now
    tournament_controller = TournamentController(tournament_model, None)
    view = PlayerView(player_controller, tournament_controller)
    player_controller.view = view  # Set view in controller after its creation
    tournament_controller.view = view  # Set view in controller after its creation
    view.main_loop()

if __name__ == "__main__":
    main()
