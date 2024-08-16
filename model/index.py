import json
import os
import uuid
from datetime import datetime
import random

class PlayerModel:
    def __init__(self, db_path='data/players.json'):
        self.db_path = db_path
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        if not os.path.exists(self.db_path):
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            with open(self.db_path, 'w') as file:
                json.dump([], file)

    def load_data(self):
        with open(self.db_path, 'r') as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.db_path, 'w') as file:
            json.dump(data, file, indent=4)

    def add_player(self, player):
        data = self.load_data()
        data.append(player)
        self.save_data(data)

    def get_players(self):
        return self.load_data()

class TournamentModel:
    def __init__(self, db_path='data/tournaments.json'):
        self.db_path = db_path
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        if not os.path.exists(self.db_path):
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            with open(self.db_path, 'w') as file:
                json.dump([], file)

    def load_data(self):
        with open(self.db_path, 'r') as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.db_path, 'w') as file:
            json.dump(data, file, indent=4)

    def add_tournament(self, tournament):
        data = self.load_data()
        data.append(tournament)
        self.save_data(data)

    def add_player_to_tournament(self, tournament_id, player_id):
        data = self.load_data()
        for tournament in data:
            if tournament["id"] == tournament_id:
                if "players" not in tournament:
                    tournament["players"] = []
                tournament["players"].append(player_id)
                break
        self.save_data(data)

    def add_round_to_tournament(self, tournament_id):
        data = self.load_data()
        for tournament in data:
            if tournament["id"] == tournament_id:
                if "rounds" not in tournament:
                    tournament["rounds"] = []

                current_round_number = len(tournament["rounds"]) + 1
                round_name = f"Round {current_round_number}"

                # For the first round, shuffle the players
                if current_round_number == 1:
                    if "players" not in tournament or len(tournament["players"]) < 2:
                        raise ValueError("Not enough players to start the first round.")
                    
                    shuffled_players = tournament["players"][:]
                    random.shuffle(shuffled_players)  # Shuffle the players
                    
                    # Pair the players for matches (assumes an even number of players)
                    matchups = []
                    for i in range(0, len(shuffled_players), 2):
                        matchups.append((shuffled_players[i], shuffled_players[i + 1]))
                    
                    round_info = {"name": round_name, "matchups": matchups}
                else:
                    round_info = {"name": round_name}

                # Add round information to the tournament
                tournament["rounds"].append(round_info)
                tournament["current_round"] = current_round_number  # Update current round

                break
        self.save_data(data)

    def get_tournaments(self):
        return self.load_data()
