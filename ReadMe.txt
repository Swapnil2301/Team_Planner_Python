```
# FactWise Assessment Project

## Overview

This project is a RESTful API implemented using Flask for managing users and teams. The API provides endpoints to create, update, list, describe, and delete users, as well as create and manage teams.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (optional but recommended)

### Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/factwise_assessment.git
cd factwise_assessment
```

2. **Create and activate a virtual environment**:

For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install the dependencies**:

```bash
pip install -r requirements.txt
```

### Running the Application

1. **Set the FLASK_APP environment variable**:

For Windows:
```bash
set FLASK_APP=app.py
```

For macOS/Linux:
```bash
export FLASK_APP=app.py
```

2. **Run the Flask application**:

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### User Management

- **Create User**: `POST /users/create`
  - Request Body: JSON with user details
  - Response: Created user details

- **Update User**: `PUT /users/update/<user_id>`
  - Request Body: JSON with updated user details
  - Response: Updated user details

- **List Users**: `GET /users/list`
  - Response: List of all users

- **Describe User**: `GET /users/describe/<user_id>`
  - Response: Details of the specified user

- **Delete User**: `DELETE /users/delete/<user_id>`
  - Response: Deletion status

### Team Management

- **Create Team**: `POST /teams/create`
  - Request Body: JSON with team details
  - Response: Created team details

## Error Handling

Common HTTP status codes that might be returned by the API:
- `200 OK`: The request was successful.
- `201 Created`: A resource was successfully created.
- `400 Bad Request`: The request could not be understood or was missing required parameters.
- `404 Not Found`: Resource not found.
- `500 Internal Server Error`: An error occurred on the server.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.