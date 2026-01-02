import pytest
from unittest.mock import patch
from src.todo.service import TodoService
from src.ui.menu import Menu


def test_mark_todo_complete_integration():
    """
    Integration test for marking todo complete workflow.
    
    Tests the integration between UI and service layers when marking a todo as complete.
    """
    service = TodoService()
    menu = Menu(service)
    
    # Add a todo to test with
    todo_id = service.add_todo("Test todo")
    
    # Mock user input for the todo ID
    with patch('builtins.input', side_effect=[str(todo_id)]):
        # Capture printed output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        menu.handle_mark_complete()
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Verify the todo was marked as complete in the service
        updated_todo = service.get_todo_by_id(todo_id)
        assert updated_todo.completed == True
        
        # Verify success message was printed
        output = captured_output.getvalue()
        assert "marked as completed" in output