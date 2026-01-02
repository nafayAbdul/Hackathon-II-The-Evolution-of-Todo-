import pytest
from src.todo.service import TodoService
from src.todo.model import Todo


class TestTodoService:
    """
    Unit tests for the TodoService.
    """
    
    def setup_method(self):
        """
        Set up a fresh TodoService instance for each test.
        """
        self.service = TodoService()
    
    def test_add_todo_success(self):
        """
        Test adding a todo successfully.
        """
        title = "Test todo"
        todo_id = self.service.add_todo(title)
        
        assert todo_id == 1  # First todo should have ID 1
        assert len(self.service.todos) == 1
        assert self.service.todos[1].title == title
        assert self.service.todos[1].completed == False
    
    def test_add_todo_empty_title(self):
        """
        Test adding a todo with an empty title raises ValueError.
        """
        with pytest.raises(ValueError, match="Todo title cannot be empty or contain only whitespace"):
            self.service.add_todo("")
    
    def test_add_todo_whitespace_only_title(self):
        """
        Test adding a todo with a whitespace-only title raises ValueError.
        """
        with pytest.raises(ValueError, match="Todo title cannot be empty or contain only whitespace"):
            self.service.add_todo("   ")
    
    def test_get_all_todos_empty(self):
        """
        Test getting all todos when the list is empty.
        """
        todos = self.service.get_all_todos()
        
        assert len(todos) == 0
        assert todos == []
    
    def test_get_all_todos_with_items(self):
        """
        Test getting all todos when there are items.
        """
        self.service.add_todo("First todo")
        self.service.add_todo("Second todo")
        
        todos = self.service.get_all_todos()
        
        assert len(todos) == 2
        assert todos[0].id == 1
        assert todos[0].title == "First todo"
        assert todos[1].id == 2
        assert todos[1].title == "Second todo"
    
    def test_get_todo_by_id_success(self):
        """
        Test getting a todo by ID successfully.
        """
        todo_id = self.service.add_todo("Test todo")
        todo = self.service.get_todo_by_id(todo_id)
        
        assert todo.id == todo_id
        assert todo.title == "Test todo"
    
    def test_get_todo_by_id_not_found(self):
        """
        Test getting a todo by a non-existent ID raises ValueError.
        """
        with pytest.raises(ValueError, match="No todo with ID 999 exists"):
            self.service.get_todo_by_id(999)
    
    def test_update_todo_success(self):
        """
        Test updating a todo successfully.
        """
        todo_id = self.service.add_todo("Original title")
        success = self.service.update_todo(todo_id, "Updated title")
        
        assert success == True
        assert self.service.todos[todo_id].title == "Updated title"
    
    def test_update_todo_not_found(self):
        """
        Test updating a non-existent todo raises ValueError.
        """
        with pytest.raises(ValueError, match="No todo with ID 999 exists"):
            self.service.update_todo(999, "New title")
    
    def test_update_todo_empty_title(self):
        """
        Test updating a todo with an empty title raises ValueError.
        """
        todo_id = self.service.add_todo("Original title")
        
        with pytest.raises(ValueError, match="Todo title cannot be empty or contain only whitespace"):
            self.service.update_todo(todo_id, "")
    
    def test_update_todo_whitespace_only_title(self):
        """
        Test updating a todo with a whitespace-only title raises ValueError.
        """
        todo_id = self.service.add_todo("Original title")
        
        with pytest.raises(ValueError, match="Todo title cannot be empty or contain only whitespace"):
            self.service.update_todo(todo_id, "   ")
    
    def test_mark_todo_complete(self):
        """
        Test marking a todo as completed.
        """
        todo_id = self.service.add_todo("Test todo")
        success = self.service.mark_todo_complete(todo_id, True)
        
        assert success == True
        assert self.service.todos[todo_id].completed == True
    
    def test_mark_todo_incomplete(self):
        """
        Test marking a todo as incomplete.
        """
        todo_id = self.service.add_todo("Test todo")
        # First mark as complete
        self.service.mark_todo_complete(todo_id, True)
        # Then mark as incomplete
        success = self.service.mark_todo_complete(todo_id, False)
        
        assert success == True
        assert self.service.todos[todo_id].completed == False
    
    def test_mark_todo_not_found(self):
        """
        Test marking a non-existent todo raises ValueError.
        """
        with pytest.raises(ValueError, match="No todo with ID 999 exists"):
            self.service.mark_todo_complete(999, True)
    
    def test_delete_todo_success(self):
        """
        Test deleting a todo successfully.
        """
        todo_id = self.service.add_todo("Test todo")
        success = self.service.delete_todo(todo_id)
        
        assert success == True
        assert len(self.service.todos) == 0
        assert todo_id not in self.service.todos
    
    def test_delete_todo_not_found(self):
        """
        Test deleting a non-existent todo raises ValueError.
        """
        with pytest.raises(ValueError, match="No todo with ID 999 exists"):
            self.service.delete_todo(999)
    
    def test_next_id_increments(self):
        """
        Test that the next ID increments properly.
        """
        first_id = self.service.add_todo("First todo")
        second_id = self.service.add_todo("Second todo")
        
        assert first_id == 1
        assert second_id == 2
        assert self.service.next_id == 3