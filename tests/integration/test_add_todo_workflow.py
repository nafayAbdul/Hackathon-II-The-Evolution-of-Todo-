import pytest
from unittest.mock import patch
from src.todo.service import TodoService
from src.ui.menu import Menu


def test_add_todo_integration():
    """
    Integration test for adding a todo workflow.
    
    Tests the integration between UI and service layers when adding a todo.
    """
    service = TodoService()
    menu = Menu(service)
    
    # Mock user input for the title
    with patch('builtins.input', return_value='New todo item'):
        # Capture printed output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        menu.handle_add_todo()
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Verify the todo was added to the service
        todos = service.get_all_todos()
        assert len(todos) == 1
        assert todos[0].title == 'New todo item'
        assert todos[0].completed == False
        
        # Verify success message was printed
        output = captured_output.getvalue()
        assert "Todo added successfully" in output