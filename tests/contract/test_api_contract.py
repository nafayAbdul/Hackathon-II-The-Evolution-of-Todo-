import pytest
from src.todo.service import TodoService


def test_api_contract():
    """
    Contract test for the entire Todo API.
    
    Verifies that all functions in the TodoService work together as expected.
    """
    service = TodoService()
    
    # Test adding multiple todos
    id1 = service.add_todo("First todo")
    id2 = service.add_todo("Second todo")
    id3 = service.add_todo("Third todo")
    
    # Verify all todos exist
    all_todos = service.get_all_todos()
    assert len(all_todos) == 3
    
    # Verify we can get a specific todo
    todo = service.get_todo_by_id(id2)
    assert todo.id == id2
    assert todo.title == "Second todo"
    
    # Test updating a todo
    success = service.update_todo(id2, "Updated second todo")
    assert success == True
    
    # Verify the update worked
    updated_todo = service.get_todo_by_id(id2)
    assert updated_todo.title == "Updated second todo"
    
    # Test marking as complete
    success = service.mark_todo_complete(id1, True)
    assert success == True
    
    # Verify the completion status was updated
    completed_todo = service.get_todo_by_id(id1)
    assert completed_todo.completed == True
    
    # Test marking as incomplete
    success = service.mark_todo_complete(id1, False)
    assert success == True
    
    # Verify the completion status was updated
    incomplete_todo = service.get_todo_by_id(id1)
    assert incomplete_todo.completed == False
    
    # Test deleting a todo
    success = service.delete_todo(id2)
    assert success == True
    
    # Verify the todo was deleted
    all_todos_after_delete = service.get_all_todos()
    assert len(all_todos_after_delete) == 2
    
    # Verify the deleted todo is gone
    with pytest.raises(ValueError):
        service.get_todo_by_id(id2)
    
    # Verify other todos still exist
    remaining_todo1 = service.get_todo_by_id(id1)
    remaining_todo3 = service.get_todo_by_id(id3)
    assert remaining_todo1.title == "First todo"
    assert remaining_todo3.title == "Third todo"