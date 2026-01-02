from typing import List, Optional
from .model import Todo
from datetime import datetime


class TodoService:
    """
    Service class to handle all todo-related operations.
    """

    def __init__(self):
        self.todos = {}
        self.next_id = 1

    def add_todo(self, title: str) -> int:
        """
        Add a new todo item.

        Args:
            title: The title/description of the todo item

        Returns:
            The ID of the newly created todo

        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        if not title or title.strip() == "":
            raise ValueError("Todo title cannot be empty or contain only whitespace")

        todo_id = self.next_id
        self.next_id += 1

        todo = Todo(
            id=todo_id,
            title=title.strip()  # Strip whitespace from the title
        )

        self.todos[todo_id] = todo
        return todo_id

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todo items, sorted by ID.
        
        Returns:
            A list of all todo items
        """
        return sorted(self.todos.values(), key=lambda x: x.id)

    def get_todo_by_id(self, todo_id: int) -> Todo:
        """
        Get a specific todo item by its ID.
        
        Args:
            todo_id: The ID of the todo item to retrieve
            
        Returns:
            The todo item with the specified ID
            
        Raises:
            ValueError: If no todo with the given ID exists
        """
        if todo_id not in self.todos:
            raise ValueError(f"No todo with ID {todo_id} exists")
        
        return self.todos[todo_id]

    def update_todo(self, todo_id: int, new_title: str) -> bool:
        """
        Update the title of an existing todo item.

        Args:
            todo_id: The ID of the todo to update
            new_title: The new title for the todo

        Returns:
            True if the update was successful, False otherwise

        Raises:
            ValueError: If no todo with the given ID exists or if new title is empty
        """
        if todo_id not in self.todos:
            raise ValueError(f"No todo with ID {todo_id} exists")

        if not new_title or new_title.strip() == "":
            raise ValueError("Todo title cannot be empty or contain only whitespace")

        self.todos[todo_id].title = new_title.strip()  # Strip whitespace from the new title
        return True

    def mark_todo_complete(self, todo_id: int, completed: bool = True) -> bool:
        """
        Mark a todo item as completed or not completed.
        
        Args:
            todo_id: The ID of the todo to update
            completed: Whether the todo is completed (default True)
            
        Returns:
            True if the update was successful, False otherwise
            
        Raises:
            ValueError: If no todo with the given ID exists
        """
        if todo_id not in self.todos:
            raise ValueError(f"No todo with ID {todo_id} exists")
        
        self.todos[todo_id].completed = completed
        return True

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item by its ID.
        
        Args:
            todo_id: The ID of the todo to delete
            
        Returns:
            True if the deletion was successful, False otherwise
            
        Raises:
            ValueError: If no todo with the given ID exists
        """
        if todo_id not in self.todos:
            raise ValueError(f"No todo with ID {todo_id} exists")
        
        del self.todos[todo_id]
        return True