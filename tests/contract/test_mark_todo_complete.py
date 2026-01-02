import pytest
from src.todo.service import TodoService


def test_mark_todo_complete_contract():
    """
    Contract test for mark_todo_complete function.
    
    Verifies that the mark_todo_complete function:
    - Accepts a todo ID (integer) and completion status (boolean, default True) as input
    - Returns a boolean success status
    - Updates the completion status of the specified todo
    - Raises ValueError for non-existent todo IDs
    """
    service = TodoService()
    
    # Add a todo to test with
    todo_id = service.add_todo("Test todo")
    
    # Verify initial state
    todo = service.get_todo_by_id(todo_id)
    assert todo.completed == False
    
    # Test marking as complete (default behavior)
    success = service.mark_todo_complete(todo_id)
    assert success == True
    
    # Verify the todo is now marked as complete
    updated_todo = service.get_todo_by_id(todo_id)
    assert updated_todo.completed == True
    
    # Test marking as incomplete
    success = service.mark_todo_complete(todo_id, False)
    assert success == True
    
    # Verify the todo is now marked as incomplete
    updated_todo = service.get_todo_by_id(todo_id)
    assert updated_todo.completed == False
    
    # Test with non-existent ID raises ValueError
    with pytest.raises(ValueError):
        service.mark_todo_complete(999)
    
    # Test with non-existent ID and explicit status raises ValueError
    with pytest.raises(ValueError):
        service.mark_todo_complete(999, True)