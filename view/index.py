import uuid

class PlayerView:
    @staticmethod
    def display_players(players):
        for player in players:
            print(f"ID: {player['id']}, Name: {player['username']}, National chess ID: {player['nationalChessID']}")

    @staticmethod

    def display_message(message):
        print(message)

    def main(self):
        while True:
            print("\nPlayer Management System")
            print("1. Add Player")
            print("2. Show Players")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                id = str(uuid.uuid4())
                name = input("Enter player name: ")
                position = input("Enter player position: ")
                player = {"id": id, "name": name, "position": position}
                self.controller.add_player(player)
            elif choice == '2':
                self.controller.show_players()
            elif choice == '3':
                break
            else:
                self.display_message("Invalid choice! Please try again.")

class TournamentView:
    @staticmethod
    def display_message(message):
        print(message)

class RoundView:
    @staticmethod
    def display_message(message):
        print(message)