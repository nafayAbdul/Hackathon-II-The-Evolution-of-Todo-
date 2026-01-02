import pytest
from src.todo.service import TodoService
from src.todo.model import Todo


def test_get_all_todos_contract():
    """
    Contract test for get_all_todos function.
    
    Verifies that the get_all_todos function:
    - Accepts no input parameters
    - Returns a list of Todo objects
    - Returns all todos sorted by ID
    - Returns an empty list when no todos exist
    """
    service = TodoService()
    
    # Test with no todos
    todos = service.get_all_todos()
    assert isinstance(todos, list)
    assert len(todos) == 0
    
    # Add some todos
    id1 = service.add_todo("First todo")
    id3 = service.add_todo("Third todo")
    id2 = service.add_todo("Second todo")
    
    # Get all todos
    todos = service.get_all_todos()
    
    # Verify return type
    assert isinstance(todos, list)
    
    # Verify all todos are returned
    assert len(todos) == 3
    
    # Verify todos are sorted by ID (1, 2, 3)
    assert todos[0].id == id1  # Smallest ID
    assert todos[1].id == id3  # Middle ID
    assert todos[2].id == id2  # Largest ID

    # Verify properties of each todo
    assert todos[0].title == "First todo"
    assert todos[1].title == "Third todo"
    assert todos[2].title == "Second todo"