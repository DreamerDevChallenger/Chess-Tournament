import json
import os

class PlayerModel:
    def __init__(self, db_path='db/user.json'):
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

class RoundModel:
    def __init__(self, db_path=''):
      self.db_path = db_path

class TournamentModel:
  def __init__(self, db_path=''):
    self.db_path = db_path