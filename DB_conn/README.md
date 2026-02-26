# FastAPI Database Connection Project

A sample FastAPI backend application that demonstrates clean architecture, scalable folder structure, and PostgreSQL database integration using SQLAlchemy.

## Features
- **FastAPI** for high-performance async API.
- **SQLAlchemy** for ORM and PostgreSQL integration.
- **Pydantic** for schema validation.
- Clean and scalable directory structure.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd DB_conn
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv .venv
   
   # For Windows
   .\.venv\Scripts\activate
   
   # For macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Copy the example environment file and update the variables for your local PostgreSQL database:
   ```bash
   cp .env.example .env
   ```
   *Edit `.env` to include your valid database credentials.*

5. **Run the server:**
   ```bash
   uvicorn src.main:app --reload
   ```

6. **Go to API Documentation:**
   Open http://127.0.0.1:8000/docs in your browser to view the interactive Swagger output.
