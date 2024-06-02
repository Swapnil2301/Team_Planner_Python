import json
import os
from base_class.user_base import BaseUserManager
DB_DIR = "db"
USERS_FILE = os.path.join(DB_DIR, "users.json")

class UserManager(BaseUserManager):
    def __init__(self):
        os.makedirs(DB_DIR, exist_ok=True)
        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'w') as f:
                json.dump({}, f)
        self.users = self._load_users()

    def _load_users(self):
        with open(USERS_FILE, 'r') as file:
            return json.load(file)

    def _save_users(self):
        with open(USERS_FILE, 'w') as file:
            json.dump(self.users, file, indent=4)

    def create_user(self, request: str) -> str:
        user_info = json.loads(request)
        user_id = user_info.get("user_id")
        if user_id in self.users:
            raise ValueError("User already exists")

        self.users[user_id] = {
            "name": user_info.get("name"),
            "email": user_info.get("email")
        }
        self._save_users()
        return json.dumps({"status": "User created successfully"})

    def list_users(self, request: str) -> str:
        return json.dumps(list(self.users.keys()))

    def describe_user(self, request: str) -> str:
        user_id = request
        if user_id not in self.users:
            raise ValueError("User not found")
        return json.dumps(self.users[user_id])

    def update_user(self, request: str) -> str:
        user_info = json.loads(request)
        user_id = user_info.get("user_id")
        if user_id not in self.users:
            raise ValueError("User not found")

        self.users[user_id]["name"] = user_info.get("name")
        self.users[user_id]["email"] = user_info.get("email")
        self._save_users()
        return json.dumps({"status": "User updated successfully"})

    def get_user(self, user_id: str) -> str:
        if user_id not in self.users:
            raise ValueError("User not found")
        return json.dumps(self.users[user_id])

    def get_user_teams(self, user_id: str) -> str:
        # Implement logic to get user's teams here
        return json.dumps({"teams": []})

    def delete_user(self, user_id):
        if user_id not in self.users:
            raise ValueError("User not found")
        del self.users[user_id]
        return {'status': 'User deleted successfully'}