from model.index import PlayerModel, TournamentModel
from view.index import PlayerView
from controller.index import PlayerController, TournamentController


def main():
    """This is the main app that return the program
    """    
    player_model = PlayerModel()
    tournament_model = TournamentModel()
    player_controller = PlayerController(player_model, None)
    tournament_controller = TournamentController(tournament_model, None)
    view = PlayerView(player_controller, tournament_controller)
    player_controller.view = view
    tournament_controller.view = view
    view.main_loop()


if __name__ == "__main__":
    main()
