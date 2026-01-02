import pytest
from src.todo.service import TodoService


def test_delete_todo_contract():
    """
    Contract test for delete_todo function.
    
    Verifies that the delete_todo function:
    - Accepts a todo ID (integer) as input
    - Returns a boolean success status
    - Removes the specified todo from the collection
    - Raises ValueError for non-existent todo IDs
    """
    service = TodoService()
    
    # Add a todo to test with
    todo_id = service.add_todo("Test todo to delete")
    
    # Verify the todo exists initially
    assert len(service.todos) == 1
    assert todo_id in service.todos
    
    # Test successful deletion
    success = service.delete_todo(todo_id)
    assert success == True
    
    # Verify the todo was removed
    assert len(service.todos) == 0
    assert todo_id not in service.todos
    
    # Test with non-existent ID raises ValueError
    with pytest.raises(ValueError):
        service.delete_todo(999)
    
    # Add another todo to test multiple deletions
    todo_id1 = service.add_todo("First todo")
    todo_id2 = service.add_todo("Second todo")
    assert len(service.todos) == 2
    
    # Delete one of them
    success = service.delete_todo(todo_id1)
    assert success == True
    assert len(service.todos) == 1
    assert todo_id1 not in service.todos
    assert todo_id2 in service.todos