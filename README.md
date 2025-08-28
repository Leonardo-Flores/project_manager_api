# Portfolio CMS API

A backend API service for a portfolio website, built with FastAPI and PostgreSQL. It provides a simple Content Management System (CMS) for managing portfolio projects.

## Features

- **Project Management:** Full CRUD (Create, Read, Update, Delete) functionality for portfolio projects.
- **Secure Endpoints:** Write operations (POST, PUT, DELETE) are protected and require a JWT token.
- **Public Endpoints:** Read operations (GET) are public for easy consumption by a frontend application.
- **Modern Tech Stack:** Built with FastAPI, SQLModel, and Pydantic for a robust and efficient API.
- **Containerized:** Fully containerized with Docker and Docker Compose for easy setup and deployment.

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLModel
- **Data Validation:** Pydantic
- **Containerization:** Docker, Docker Compose

## Project Structure

The project follows a standard structure for FastAPI applications to ensure code is organized, scalable, and maintainable.

```
.
├── app/                  # Main application source code
│   ├── api/              # API specific modules (routers, endpoints)
│   │   └── v1/           # Version 1 of the API
│   ├── core/             # Application settings and configuration
│   ├── crud/             # CRUD database operations
│   ├── db/               # Database session management
│   ├── models/           # SQLModel database models
│   ├── schemas/          # Pydantic data schemas
│   ├── dependencies.py   # Dependency injection functions (e.g., security)
│   └── main.py           # FastAPI application entry point
├── .env                  # Environment variables (credentials, DB URL)
├── Dockerfile            # Dockerfile for building the API image
├── docker-compose.yml    # Docker Compose file for orchestration
└── requirements.txt      # Python dependencies
```

## Getting Started

You can run this project in two ways: using Docker (recommended) or setting it up locally.

### 1. Running with Docker (Recommended)

This is the simplest way to get the application and database running.

**Prerequisites:**
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

**Steps:**

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Environment Variables:**
    The repository includes a `.env` file with default settings. You can review and modify it if needed. The default password is `a_secure_password`. It is recommended to change this for a production environment.

3.  **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```
    The `--build` flag ensures the API image is built from the Dockerfile. You only need to use it the first time or when you change the code or dependencies.

The API will be available at `http://localhost:8000`. You can access the interactive API documentation at `http://localhost:8000/docs`.

### 2. Running Locally (Without Docker)

If you prefer to run the application directly on your machine.

**Prerequisites:**
- Python 3.9+
- A running PostgreSQL instance.

**Steps:**

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the database:**
    - Make sure your PostgreSQL server is running.
    - Create a new database, user, and password.
    - Update the `.env` file with your local PostgreSQL connection details. For example:
      `DATABASE_URL=postgresql://myuser:mypassword@localhost:5432/mydatabase`

5.  **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The `--reload` flag automatically reloads the server when you make code changes.

The API will be available at `http://localhost:8000`.

## API Endpoints

All endpoints are available under the `/api/v1` prefix.

| Method   | Endpoint             | Protection | Description                      |
|----------|----------------------|------------|----------------------------------|
| `GET`    | `/projects/`         | Public     | Get a list of all projects.      |
| `GET`    | `/projects/{id}`     | Public     | Get a single project by its ID.  |
| `POST`   | `/projects/`         | **Protected**  | Create a new project.            |
| `PUT`    | `/projects/{id}`     | **Protected**  | Update an existing project.      |
| `DELETE` | `/projects/{id}`     | **Protected**  | Delete a project by its ID.      |

**Note on Protected Endpoints:**
To access protected endpoints, you must provide a valid JWT Bearer token in the `Authorization` header. Token generation is handled by a separate authentication service.

## Environment Variables

The application is configured using environment variables, which are defined in the `.env` file.

- `POSTGRES_USER`: The username for the PostgreSQL database.
- `POSTGRES_PASSWORD`: The password for the PostgreSQL user.
- `POSTGRES_DB`: The name of the PostgreSQL database.
- `POSTGRES_SERVER`: The hostname of the database server (defaults to `db` for Docker).
- `POSTGRES_PORT`: The port of the database server.
- `DATABASE_URL`: The full connection string for the database, used by the application.
