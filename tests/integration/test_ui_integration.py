import pytest
from unittest.mock import patch
from io import StringIO
import sys
from src.todo.service import TodoService
from src.ui.menu import Menu


def test_ui_integration():
    """
    Integration test for the UI components.
    
    Tests the integration between UI and service layers for all operations.
    """
    service = TodoService()
    menu = Menu(service)
    
    # Test adding a todo
    with patch('builtins.input', return_value='Test todo'):
        captured_output = StringIO()
        sys.stdout = captured_output
        menu.handle_add_todo()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        assert "Todo added successfully" in output
    
    # Verify the todo was added
    todos = service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].title == "Test todo"
    
    # Test viewing todos
    captured_output = StringIO()
    sys.stdout = captured_output
    menu.handle_view_todos()
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert "Test todo" in output
    
    # Test updating the todo
    with patch('builtins.input', side_effect=['1', 'Updated todo']):
        captured_output = StringIO()
        sys.stdout = captured_output
        menu.handle_update_todo()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        assert "updated successfully" in output
    
    # Verify the todo was updated
    todos = service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].title == "Updated todo"
    
    # Test marking as complete
    with patch('builtins.input', side_effect=['1']):
        captured_output = StringIO()
        sys.stdout = captured_output
        menu.handle_mark_complete()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        assert "marked as completed" in output
    
    # Verify the todo is marked complete
    todos = service.get_all_todos()
    assert len(todos) == 1
    assert todos[0].completed == True
    
    # Test deleting the todo
    with patch('builtins.input', side_effect=['1', 'y']):
        captured_output = StringIO()
        sys.stdout = captured_output
        menu.handle_delete_todo()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        assert "deleted successfully" in output
    
    # Verify the todo was deleted
    todos = service.get_all_todos()
    assert len(todos) == 0