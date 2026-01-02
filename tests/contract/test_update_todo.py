import pytest
from src.todo.service import TodoService


def test_update_todo_contract():
    """
    Contract test for update_todo function.
    
    Verifies that the update_todo function:
    - Accepts a todo ID (integer) and new title (string) as input
    - Returns a boolean success status
    - Updates the title of the specified todo
    - Raises ValueError for non-existent todo IDs
    - Raises ValueError for empty or whitespace-only new titles
    """
    service = TodoService()
    
    # Add a todo to test with
    todo_id = service.add_todo("Original title")
    
    # Test successful update
    new_title = "Updated title"
    success = service.update_todo(todo_id, new_title)
    assert success == True
    
    # Verify the todo was updated
    updated_todo = service.get_todo_by_id(todo_id)
    assert updated_todo.title == new_title
    
    # Test with non-existent ID raises ValueError
    with pytest.raises(ValueError):
        service.update_todo(999, "New title")
    
    # Test with empty new title raises ValueError
    with pytest.raises(ValueError):
        service.update_todo(todo_id, "")
    
    # Test with whitespace-only new title raises ValueError
    with pytest.raises(ValueError):
        service.update_todo(todo_id, "   ")
    
    # Test with valid new title that has leading/trailing whitespace (should be trimmed by service)
    title_with_spaces = "  Updated title with spaces  "
    success = service.update_todo(todo_id, title_with_spaces)
    assert success == True
    updated_todo = service.get_todo_by_id(todo_id)
    # Verify the service trims the title
    assert updated_todo.title == title_with_spaces.strip()