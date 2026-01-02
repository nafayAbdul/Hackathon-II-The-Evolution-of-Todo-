import pytest
from unittest.mock import patch
from src.todo.service import TodoService
from src.ui.menu import Menu


def test_update_todo_integration():
    """
    Integration test for updating todo workflow.
    
    Tests the integration between UI and service layers when updating a todo.
    """
    service = TodoService()
    menu = Menu(service)
    
    # Add a todo to test with
    todo_id = service.add_todo("Original todo")
    
    # Mock user input for the todo ID and new title
    with patch('builtins.input', side_effect=[str(todo_id), "Updated todo"]):
        # Capture printed output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        menu.handle_update_todo()
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Verify the todo was updated in the service
        updated_todo = service.get_todo_by_id(todo_id)
        assert updated_todo.title == "Updated todo"
        
        # Verify success message was printed
        output = captured_output.getvalue()
        assert "updated successfully" in output