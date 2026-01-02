import pytest
from unittest.mock import patch
from src.todo.service import TodoService
from src.ui.menu import Menu


def test_delete_todo_integration():
    """
    Integration test for deleting todo workflow.
    
    Tests the integration between UI and service layers when deleting a todo.
    """
    service = TodoService()
    menu = Menu(service)
    
    # Add a todo to test with
    todo_id = service.add_todo("Todo to delete")
    
    # Verify the todo exists initially
    assert len(service.get_all_todos()) == 1
    
    # Mock user input for the todo ID and confirmation
    with patch('builtins.input', side_effect=[str(todo_id), "y"]):
        # Capture printed output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        menu.handle_delete_todo()
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Verify the todo was deleted from the service
        assert len(service.get_all_todos()) == 0
        
        # Verify success message was printed
        output = captured_output.getvalue()
        assert "deleted successfully" in output