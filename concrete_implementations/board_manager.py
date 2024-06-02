import json
import os
from base_class.base_board_manager import BaseBoardManager

DB_DIR = "db"
BOARDS_FILE = os.path.join(DB_DIR, "boards.json")
TASKS_FILE = os.path.join(DB_DIR, "tasks.json")

class BoardManager(BaseBoardManager):
    def __init__(self):
        os.makedirs(DB_DIR, exist_ok=True)
        if not os.path.exists(BOARDS_FILE):
            with open(BOARDS_FILE, 'w') as f:
                json.dump({}, f)
        if not os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'w') as f:
                json.dump({}, f)
        self.boards = self._load_boards()
        self.tasks = self._load_tasks()

    def _load_boards(self):
        with open(BOARDS_FILE, 'r') as f:
            return json.load(f)

    def _save_boards(self, boards):
        with open(BOARDS_FILE, 'w') as f:
            json.dump(boards, f, indent=4)

    def _load_tasks(self):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)

    def _save_tasks(self, tasks):
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)

    def create_board(self, request: str) -> str:
        req = json.loads(request)
        board_id = req.get("board_id")
        board_name = req.get("board_name")
        tasks = req.get("tasks", [])

        if board_id in self.boards:
            raise ValueError("Board ID already exists")

        self.boards[board_id] = {
            "board_name": board_name,
            "tasks": tasks
        }
        self._save_boards(self.boards)
        return json.dumps({"status": "Board created successfully"})

    def add_task(self, board_id: str, request: str) -> str:
        if board_id not in self.boards:
            raise ValueError("Board not found")

        task_info = json.loads(request)
        task_id = task_info.get("task_id")
        if task_id in self.tasks:
            raise ValueError("Task ID already exists")

        self.tasks[task_id] = task_info
        self.boards[board_id]["tasks"].append(task_id)
        self._save_tasks(self.tasks)
        self._save_boards(self.boards)
        return json.dumps({"status": "Task added successfully"})

    def get_task(self, board_id: str, task_id: str) -> str:
        if board_id not in self.boards:
            raise ValueError("Board not found")

        if task_id not in self.tasks:
            raise ValueError("Task not found")

        return json.dumps(self.tasks[task_id])

    def update_task(self, board_id: str, task_id: str, request: str) -> str:
        if board_id not in self.boards:
            raise ValueError("Board not found")

        if task_id not in self.tasks:
            raise ValueError("Task not found")

        updated_task_info = json.loads(request)
        self.tasks[task_id] = updated_task_info
        self._save_tasks(self.tasks)
        return json.dumps({"status": "Task updated successfully"})

    def delete_task(self, board_id: str, task_id: str) -> str:
        if board_id not in self.boards:
            raise ValueError("Board not found")

        if task_id not in self.tasks:
            raise ValueError("Task not found")

        del self.tasks[task_id]
        self.boards[board_id]["tasks"].remove(task_id)
        self._save_tasks(self.tasks)
        self._save_boards(self.boards)
        return json.dumps({"status": "Task deleted successfully"})
