import uuid


class PlayerView:
    def __init__(self, player_controller, tournament_controller):
        self.player_controller = player_controller
        self.tournament_controller = tournament_controller

    @staticmethod
    def display_players(players):
        for player in players:
            print(
                f"Chess ID: {player['id']}, Firstname: {player['firstname']}, Lastname: {player['lastname']}"
            )

    @staticmethod
    def display_tournaments(tournaments):
        for tournament in tournaments:
            print(
                f"ID: {tournament['id']}, Name: {tournament['name']}, Location: {tournament['location']}, "
                f"Start Date: {tournament['start_date']}, End Date: {tournament['end_date']}, "
                f"Rounds: {tournament.get('rounds', [])}, Current Round: {tournament['current_round']}, "
                f"Registered Players: {tournament.get('players', [])}, Remarks: {tournament['description']}"
            )

            for round_info in tournament.get("rounds", []):
                print(f"{round_info['name']}")
                if "matchups" in round_info:
                    for match in round_info["matchups"]:
                        print(f"Match: Player {match[0][0]} (Score: {match[0][1]}) vs "
                              f"Player {match[1][0]} (Score: {match[1][1]})")
                else:
                    print("No matchups for this round.")

    @staticmethod
    def display_message(message):
        print(message)

    def main_loop(self):
        while True:
            print("\nChess Tournament Management System")
            print("1. Add Player")
            print("2. Show Players")
            print("3. Add Tournament")
            print("4. Show Tournaments")
            print("5. Add Player to Tournament")
            print("6. Add Round to Tournament")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                id = input("Enter chess ID: ")
                firstname = input("Enter player firstname: ")
                lastname = input("Enter player lastname: ")
                birthdate = input("Enter player birthdate: ")

                player = {
                    "id": id,
                    "firstname": firstname,
                    "lastname": lastname,
                    "birthdate": birthdate,
                }
                self.player_controller.add_player(player)
            elif choice == "2":
                self.player_controller.show_players()
            elif choice == "3":
                id = str(uuid.uuid4())
                name = input("Enter tournament name: ")
                location = input("Enter tournament location: ")
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                num_revolutions = (
                    input("Enter number of revolutions (default 4): ") or 4
                )
                description = input("Enter tournament description: ")
                tournament = {
                    "id": id,
                    "name": name,
                    "location": location,
                    "start_date": start_date,
                    "end_date": end_date,
                    "num_revolutions": int(num_revolutions),
                    "current_round": 0,
                    "rounds": [],
                    "players": [],
                    "description": description,
                }
                self.tournament_controller.add_tournament(tournament)
            elif choice == "4":
                self.tournament_controller.show_tournaments()
            elif choice == "5":
                tournament_id = input("Enter tournament ID: ")
                player_id = input("Enter player ID: ")
                self.tournament_controller.add_player_to_tournament(
                    tournament_id, player_id
                )
            elif choice == "6":
                tournament_id = input("Enter tournament ID: ")
                round_number = input("Enter round number: ")
                round_info = {"round_number": round_number}
                self.tournament_controller.add_round_to_tournament(
                    tournament_id, round_info
                )
            elif choice == "7":
                break
            else:
                self.display_message("Invalid choice! Please try again.")
