from abc import ABC, abstractmethod


class BaseUserManager(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create_user(self, request: str) -> str:
        pass

    @abstractmethod
    def list_users(self, request:str) -> str:
        pass

    @abstractmethod
    def describe_user(self, request:str) -> str:
        pass

    @abstractmethod
    def update_user(self, user_id: str) -> str:
        pass

    @abstractmethod
    def get_user_teams(self, user_id: str) -> str:
        pass

