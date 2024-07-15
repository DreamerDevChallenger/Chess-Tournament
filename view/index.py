import uuid

class PlayerView:
    def __init__(self, player_controller, tournament_controller):
        self.player_controller = player_controller
        self.tournament_controller = tournament_controller
    @staticmethod
    def display_players(players):
        for player in players:
            print(f"ID: {player['id']}, Name: {player['username']}, National chess ID: {player['nationalChessID']}")

    @staticmethod 
    def display_tournaments(tournaments):
        for tournament in tournaments:
            print(f"ID: {tournament['id']}, Name: {tournament['name']}, Players: {tournament.get('players', [])}")

    @staticmethod 
    def display_message(message):
        print(message)

    def main_loop(self):
        while True:
            print("\nPlayer Management System")
            print("1. Add Player")
            print("2. Show Players")
            print("3. Add Tournament")
            print("4. Show Tournaments")
            print("5. Add Player to Tournament")
            print("6. Exit")
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
                self.player_controller.add_player(player)
            elif choice == '2':
                self.player_controller.show_players()
            elif choice == '3':
                id = str(uuid.uuid4())
                name = input("Enter tournament name: ")
                tournament = {"id": id, "name": name}
                self.tournament_controller.add_tournament(tournament)
            elif choice == '4':
                self.tournament_controller.show_tournaments()
            elif choice == '5':
                tournament_id = input("Enter tournament ID: ")
                player_id = input("Enter player ID: ")
                self.tournament_controller.add_player_to_tournament(tournament_id, player_id)
            elif choice == '6':
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