import json
import os
from base_class.team_base import BaseTeamManager

DB_DIR = "db"
TEAMS_FILE = os.path.join(DB_DIR, "teams.json")

class TeamManager(BaseTeamManager):
    def __init__(self):
        os.makedirs(DB_DIR, exist_ok=True)
        if not os.path.exists(TEAMS_FILE):
            with open(TEAMS_FILE, 'w') as f:
                json.dump({}, f)
        self.teams = self._load_teams()

    def _load_teams(self):
        with open(TEAMS_FILE, 'r') as f:
            return json.load(f)

    def _save_teams(self):
        with open(TEAMS_FILE, 'w') as f:
            json.dump(self.teams, f, indent=4)

    def create_team(self, request: str) -> str:
        team_info = json.loads(request)
        team_id = team_info.get("team_id")
        if team_id in self.teams:
            raise ValueError("Team ID already exists")

        self.teams[team_id] = {
            "team_name": team_info.get("team_name"),
            "user_ids": team_info.get("user_ids", [])
        }
        self._save_teams()
        return json.dumps({"status": "Team created successfully"})

    def list_teams(self, team_id: str, user_id: str) -> str:
        # Implement logic to list teams here
        return json.dumps(list(self.teams.keys()))

    def describe_teams(self, team_id: str, user_id: str) -> str:
        if team_id not in self.teams:
            raise ValueError("Team not found")
        return json.dumps(self.teams[team_id])

    def update_teams(self, team_id: str, user_id: str) -> str:
        if team_id not in self.teams:
            raise ValueError("Team not found")
        # Implement logic to update team information here
        return json.dumps({"status": "Team updated successfully"})

    def add_user_to_teams(self, team_id: str, user_id: str) -> str:
        if team_id not in self.teams:
            raise ValueError("Team not found")

        if user_id in self.teams[team_id]["user_ids"]:
            raise ValueError("User already in team")

        self.teams[team_id]["user_ids"].append(user_id)
        self._save_teams()
        return json.dumps({"status": "User added to team successfully"})
