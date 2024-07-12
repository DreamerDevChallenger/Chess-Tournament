from model.index import PlayerModel
from view.index import PlayerView
from controller.index import PlayerController
import uuid


def main():
    model = PlayerModel()
    view = PlayerView()
    controller = PlayerController(model, view)
    controller.view.main()

if __name__ == "__main__":
    main()
