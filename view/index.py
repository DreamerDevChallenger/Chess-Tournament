class PlayerView:
    @staticmethod
    def display_players(players):
        for player in players:
            print(f"ID: {player['id']}, Name: {player['username']}, National chess ID: {player['nationalChessID']}")

    @staticmethod
    def display_message(message):
        print(message)