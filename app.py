from flask import Flask, request, jsonify
from concrete_implementations.user_manager import UserManager
from concrete_implementations.team_manager import TeamManager
from concrete_implementations.board_manager import BoardManager

app = Flask(__name__)

user_manager = UserManager()
team_manager = TeamManager()
board_manager = BoardManager()

@app.route('/users/create', methods=['POST'])
def create_user():
    response = user_manager.create_user(request.data.decode('utf-8'))
    return response, 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    response = user_manager.describe_user(user_id)
    return response, 200

@app.route('/users/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    response = user_manager.delete_user(user_id)
    return response, 200

@app.route('/teams/create', methods=['POST'])
def create_team():
    response = team_manager.create_team(request.data.decode('utf-8'))
    return response, 200

@app.route('/teams/addUser/<team_id>', methods=['PUT'])
def add_user_to_team(team_id):
    user_id = request.json.get('user_id')
    response = team_manager.add_user_to_team(team_id, user_id)
    return response, 200

@app.route('/boards/create', methods=['POST'])
def create_board():
    response = board_manager.create_board(request.data.decode('utf-8'))
    return response, 200

@app.route('/boards/addTask/<board_id>', methods=['PUT'])
def add_task(board_id):
    response = board_manager.add_task(board_id, request.data.decode('utf-8'))
    return response, 200

@app.route('/boards/<board_id>/task/<task_id>', methods=['GET'])
def get_task(board_id, task_id):
    response = board_manager.get_task(board_id, task_id)
    return response, 200

@app.route('/boards/updateTask/<board_id>/<task_id>', methods=['PUT'])
def update_task(board_id, task_id):
    response = board_manager.update_task(board_id, task_id, request.data.decode('utf-8'))
    return response, 200

@app.route('/boards/deleteTask/<board_id>/<task_id>', methods=['DELETE'])
def delete_task(board_id, task_id):
    response = board_manager.delete_task(board_id, task_id)
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
