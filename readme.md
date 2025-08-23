# Xuanrong Backend

This repository contains the backend source code for the Xuanrong project.

## Features

- MIT licensed ([LICENSE](LICENSE))
- Organized source code in [`src/`](src/)
- Python backend (see `.gitignore` for Python-specific ignores)

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/xuanrong-backend.git
   cd xuanrong-backend
   ```

2. **Set up your environment:**
   - Create a virtual environment:
     ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install dependencies (if you have a requirements file):
     ```sh
     pip install -r requirements.txt
     ```

3. **Run the backend:**
   - (Add instructions here for running your backend, e.g. `python run.py`)


## Project Structure

```
.
├── LICENSE                     # MIT license file
├── readme.md                   # Project documentation
├── docker-compose.yml          # Docker compose configuration
├── Dockerfile                  # Docker image build instructions
├── requirements.txt            # Python dependencies
├── run.py                      # Development server entry point
├── app/                        # Main application package
│   ├── __init__.py            # Package initializer
│   ├── main.py                # FastAPI application factory
│   ├── api/                   # API layer
│   │   ├── __init__.py        # Package initializer
│   │   └── v1/                # API version 1
│   │       ├── __init__.py    # Package initializer
│   │       ├── api.py         # Main API router
│   │       └── endpoints/     # API endpoint handlers
│   │           ├── __init__.py # Package initializer
│   │           └── hello.py   # Hello world endpoints
│   ├── core/                  # Core application logic
│   │   └── __init__.py        # Package initializer
│   ├── crud/                  # Database CRUD operations
│   ├── models/                # Database models (SQLAlchemy)
│   ├── schemas/               # Pydantic models for API validation
│   │   ├── __init__.py        # Package initializer
│   │   └── hello.py           # Hello response schema
│   └── utils/                 # Utility functions and helpers
├── tests/                     # Test suite
└── venv/                      # Virtual environment (development)
```

### File Purposes

#### Core Application Files
- **`app/main.py`**: FastAPI application initialization and configuration
- **`run.py`**: Development server launcher using Uvicorn

#### API Structure
- **`app/api/v1/api.py`**: Main API router that includes all endpoint routers
- **`app/api/v1/endpoints/hello.py`**: Hello world API endpoints implementation

#### Data Models & Validation
- **`app/schemas/hello.py`**: Pydantic models for request/response validation
- **`app/models/`**: SQLAlchemy database models (future database entities)
- **`app/crud/`**: Database operations and business logic (Create, Read, Update, Delete)

#### Application Infrastructure
- **`app/core/`**: Core application settings, configuration, and utilities
- **`app/utils/`**: Helper functions and common utilities

#### Development & Deployment
- **`Dockerfile`**: Multi-stage Docker build for production deployment
- **`docker-compose.yml`**: Local development environment setup
- **`requirements.txt`**: Python package dependencies
- **`tests/`**: Unit tests, integration tests, and test utilities

## API Endpoints

The backend provides the following REST API endpoints:

### Base URL
- Local development: `http://localhost:8000`
- Docker: `http://localhost:8000`

### Available Endpoints

#### Hello World API
- **GET** `/api/v1/` - Returns a simple "Hello World" message
  - Response: `{"message": "Hello World"}`

- **GET** `/api/v1/hello/{name}` - Returns a personalized hello message
  - Parameters:
    - `name` (string): The name to include in the greeting
  - Response: `{"message": "Hello {name}"}`

#### API Documentation
- **GET** `/docs` - Interactive API documentation (Swagger UI)
- **GET** `/redoc` - Alternative API documentation (ReDoc)

## Docker Build and Run

### Build the Docker Image

To build the Docker image for the FastAPI backend, run:

```sh
docker compose build
```

### Run the Backend with Docker Compose

To start the backend service:

```sh
docker compose up
```

This will:
- Build the image if it’s not already built
- Start the container named `fastapi-xuanrong`
- Map port `8000` on your machine to port `8000` in the container
- Mount the `./app` directory as read-only inside the container
- Set the `PYTHONPATH` environment variable
- Automatically restart the container unless stopped
- Perform a healthcheck on `http://localhost:8000/api/v1/` every 30 seconds

### Stop the Backend

To stop and remove the containers:

```sh
docker compose down
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.