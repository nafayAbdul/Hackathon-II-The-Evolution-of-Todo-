import pytest
from datetime import datetime
from src.todo.model import Todo


class TestTodoModel:
    """
    Unit tests for the Todo model.
    """
    
    def test_create_todo_with_valid_data(self):
        """
        Test creating a todo with valid data.
        """
        todo = Todo(id=1, title="Test todo", completed=False)
        
        assert todo.id == 1
        assert todo.title == "Test todo"
        assert todo.completed == False
        assert isinstance(todo.created_at, datetime)
    
    def test_create_todo_defaults(self):
        """
        Test creating a todo with default values.
        """
        todo = Todo(id=1, title="Test todo")
        
        assert todo.id == 1
        assert todo.title == "Test todo"
        assert todo.completed == False
        assert isinstance(todo.created_at, datetime)
    
    def test_todo_str_representation_completed(self):
        """
        Test the string representation of a completed todo.
        """
        todo = Todo(id=1, title="Test todo", completed=True)
        expected = "[X] Test todo"
        
        assert str(todo) == expected
    
    def test_todo_str_representation_not_completed(self):
        """
        Test the string representation of an incomplete todo.
        """
        todo = Todo(id=1, title="Test todo", completed=False)
        expected = "[ ] Test todo"
        
        assert str(todo) == expected
    
    def test_todo_created_at_auto_set(self):
        """
        Test that created_at is automatically set when not provided.
        """
        before = datetime.now()
        todo = Todo(id=1, title="Test todo")
        after = datetime.now()
        
        assert todo.created_at >= before
        assert todo.created_at <= after
    
    def test_todo_created_at_explicitly_set(self):
        """
        Test that created_at can be explicitly set.
        """
        custom_time = datetime(2023, 1, 1, 12, 0, 0)
        todo = Todo(id=1, title="Test todo", created_at=custom_time)
        
        assert todo.created_at == custom_time