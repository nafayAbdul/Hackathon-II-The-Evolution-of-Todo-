# Quickstart Guide: Console-Based Todo Application

## Prerequisites
- Python 3.13+
- UV package manager (optional, for virtual environment)

## Setup
1. Clone or download the project
2. Navigate to the project directory
3. (Optional) Create a virtual environment:
   ```bash
   uv venv  # or python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies (if any):
   ```bash
   uv pip install -r requirements.txt  # if requirements file exists
   ```

## Running the Application
```bash
python src/main.py
```

## Basic Usage
1. Run the application using the command above
2. The main menu will display available options
3. Follow the on-screen prompts to:
   - Add a new todo
   - View all todos
   - Update an existing todo
   - Mark a todo as completed
   - Delete a todo
4. Type 'exit' or 'quit' to close the application

## Example Workflow
```
Welcome to the Todo Application!
1. Add a new todo
2. View all todos
3. Update a todo
4. Mark todo as completed
5. Delete a todo
6. Exit

Choose an option: 1
Enter todo description: Buy groceries
Todo added successfully!

Choose an option: 2
1. [ ] Buy groceries
```

## Testing
To run the tests:
```bash
pytest tests/
```