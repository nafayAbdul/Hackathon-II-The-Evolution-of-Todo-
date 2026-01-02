import pytest
from unittest.mock import patch
from io import StringIO
import sys
from src.todo.service import TodoService
from src.ui.menu import Menu


def test_view_todos_integration():
    """
    Integration test for viewing todos workflow.
    
    Tests the integration between UI and service layers when viewing todos.
    """
    service = TodoService()
    menu = Menu(service)
    
    # Add some todos to the service
    service.add_todo("First todo")
    service.add_todo("Second todo")
    
    # Capture printed output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    menu.handle_view_todos()
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Verify output contains the todos
    output = captured_output.getvalue()
    assert "First todo" in output
    assert "Second todo" in output
    assert "[ ]" in output  # Check for uncompleted status