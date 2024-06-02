import abc
import json

class BaseTeamManager(abc.ABC):
    @abc.abstractmethod
    def create_team(self, team_info: str) -> str:
        pass

    @abc.abstractmethod
    def list_teams(self, team_id: str, user_id: str) -> str:
        pass

    @abc.abstractmethod
    def describe_teams(self, team_id: str, user_id: str) -> str:
        pass

    @abc.abstractmethod
    def update_teams(self, team_id: str, user_id: str) -> str:
        pass

    @abc.abstractmethod
    def add_user_to_teams(self, team_id: str, user_id: str) -> str:
        pass