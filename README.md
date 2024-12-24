# TaskFlow API

A RESTful API built with Flask and SQLAlchemy that provides task management functionality with user authentication.

## Features

- User authentication with JWT tokens
- CRUD operations for task lists
- CRUD operations for individual tasks
- List and task reordering capabilities
- Task movement between lists
- Secure password hashing
- Error handling and validation
- CORS support

## Tech Stack

- **Python 3.x**
- **Flask** - Web framework
- **SQLAlchemy** - ORM for database management
- **Flask-JWT-Extended** - JWT authentication
- **Flask-CORS** - Cross-Origin Resource Sharing
- **Werkzeug** - Password hashing

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd task-management-api
```

2. Install Pipenv if you haven't already:
```bash
pip install pipenv
```

3. Install dependencies using Pipenv:
```bash
pipenv install
```

4. Activate the virtual environment:
```bash
pipenv shell
```

## Database Management Scripts

The project includes several predefined scripts for database management:

```bash
# Initialize the database
pipenv run init

# Generate a new migration
pipenv run migrate

# Apply migrations
pipenv run upgrade

# Rollback migrations
pipenv run downgrade
```

These scripts are defined in the Pipfile and can be executed using `pipenv run [script-name]`.

## API Documentation

Detailed API documentation is available in two formats:

1. Markdown format: See `api-documentation.md`
2. HTML format: Open `index.html` in your browser for a styled documentation view

### Quick Endpoint Overview:

- Authentication:
  - `POST /api/register` - Create new user
  - `POST /api/login` - User login

- Lists:
  - `POST /api/list` - Create new list
  - `GET /api/list` - Get all lists
  - `DELETE /api/list/delete` - Delete list
  - `PUT /api/list/change` - Update list title
  - `PUT /api/list/reorder` - Reorder lists

- Tasks:
  - `POST /api/task` - Create new task
  - `DELETE /api/task/delete` - Delete task
  - `PUT /api/task/change` - Update task text
  - `PUT /api/tasks/reorder` - Reorder tasks
  - `PUT /api/task/move` - Move task between lists

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the token in the Authorization header:
```
Authorization: Bearer <jwt_token>
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:
- 200: Success
- 201: Successfully created
- 400: Bad request
- 404: Resource not found
- 500: Server error

## Development

To run the development server:
```bash
pipenv run start
```

The API will be available at `http://localhost:5000`