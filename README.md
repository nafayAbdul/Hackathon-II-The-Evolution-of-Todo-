# Console Todo Application

A simple, in-memory console-based todo application built with Python.

## Features

- Add, view, update, mark complete, and delete todo items
- All data stored in memory only (no persistence after program exit)
- Clean, user-friendly console interface
- No external dependencies (uses only Python standard library)

## Prerequisites

- Python 3.13+
- UV package manager

## Setup and Installation

1. Install UV if you haven't already:
   ```bash
   pip install uv
   ```

2. Clone or download this repository

3. Navigate to the project directory

4. (Optional) Create a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

5. Install the application:
   ```bash
   uv pip install -e .
   ```

## Running the Application

### Method 1: Direct Python execution
```bash
python src/main.py
```

### Method 2: Using the installed script
```bash
todo-app
```

## Usage

Once the application is running, you'll see a menu with the following options:
1. Add a new todo
2. View all todos
3. Update a todo
4. Mark todo as completed
5. Delete a todo
6. Exit

Follow the on-screen prompts to interact with the application.

## Development

To run the tests:
```bash
# Install in development mode
uv pip install -e .[dev]

# Run all tests
pytest
```

## Architecture

The application follows a layered architecture:
- **Entry Layer**: `main.py` (application bootstrap)
- **Domain Layer**: `todo/` (models and business logic)
- **Interaction Layer**: `ui/` (console I/O handling)
- **Tests**: organized by type (unit, integration, contract)"# Hackathon-II-The-Evolution-of-Todo-"  
