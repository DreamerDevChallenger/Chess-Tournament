from model.index import PlayerModel
from view.index import PlayerView
from controller.index import PlayerController
import uuid


def main():
    model = PlayerModel()
    view = PlayerView()
    controller = PlayerController(model, view)

    while True:
        print("\nPlayer Management System")
        print("1. Add Player")
        print("2. Show Players")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            id = str(uuid.uuid4())
            nationalChessID = input("Enter national chess ID: "),
            lastname = input("Enter player lastname: ")
            firstname = input("Enter player firstname: ")
            username = input("Enter player username: ")
            player = {
                "id": id, 
                "username": username, 
                "nationalChessID": nationalChessID, 
                "firstname": firstname, 
                "lastname": lastname ,
            }
            controller.add_player(player)
        elif choice == '2':
            controller.show_players()
        elif choice == '3':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
