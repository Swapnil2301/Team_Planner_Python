import abc
import json

class BaseBoardManager(abc.ABC):
    @abc.abstractmethod
    def create_board(self, board_info: str) -> str:
        pass

    @abc.abstractmethod
    def add_task(self, board_id: str, task_info: str) -> str:
        pass

    @abc.abstractmethod
    def get_task(self, board_id: str, task_id: str) -> str:
        pass

    @abc.abstractmethod
    def update_task(self, board_id: str, task_id: str, task_info: str) -> str:
        pass

    @abc.abstractmethod
    def delete_task(self, board_id: str, task_id: str) -> str:
        pass