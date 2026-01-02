import pytest
from src.todo.service import TodoService


def test_add_todo_contract():
    """
    Contract test for add_todo function.
    
    Verifies that the add_todo function:
    - Accepts a string title as input
    - Returns an integer ID
    - Creates a todo with the specified title
    - Sets completion status to False by default
    - Raises ValueError for empty or whitespace-only titles
    """
    service = TodoService()
    
    # Test successful addition
    title = "Test todo"
    todo_id = service.add_todo(title)
    
    # Verify return value is an integer ID
    assert isinstance(todo_id, int)
    assert todo_id > 0
    
    # Verify todo was created with correct properties
    created_todo = service.get_todo_by_id(todo_id)
    assert created_todo.title == title
    assert created_todo.completed == False
    
    # Test with empty title raises ValueError
    with pytest.raises(ValueError):
        service.add_todo("")
    
    # Test with whitespace-only title raises ValueError
    with pytest.raises(ValueError):
        service.add_todo("   ")
    
    # Test with valid title that has leading/trailing whitespace (should be trimmed by service)
    title_with_spaces = "  Todo with spaces  "
    todo_id2 = service.add_todo(title_with_spaces)
    created_todo2 = service.get_todo_by_id(todo_id2)
    # Verify the service trims the title
    assert created_todo2.title == title_with_spaces.strip()