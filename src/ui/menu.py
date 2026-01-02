from typing import List
from todo.model import Todo
from todo.service import TodoService
from .input_handler import InputHandler


class Menu:
    """
    Handles the console menu interface for the todo application.
    """
    
    def __init__(self, todo_service: TodoService):
        self.todo_service = todo_service
        self.input_handler = InputHandler()

    def display_menu(self):
        """
        Display the main menu options.
        """
        print("\n" + "="*40)
        print("Welcome to the Todo Application!")
        print("="*40)
        print("1. Add a new todo")
        print("2. View all todos")
        print("3. Update a todo")
        print("4. Mark todo as completed")
        print("5. Delete a todo")
        print("6. Exit")
        print("="*40)

    def handle_add_todo(self):
        """
        Handle adding a new todo.
        """
        try:
            title = input("Enter todo description: ").strip()
            
            if not self.input_handler.validate_todo_title(title):
                print("Error: Todo title cannot be empty and must be 500 characters or less.")
                return
            
            todo_id = self.todo_service.add_todo(title)
            print(f"Todo added successfully with ID: {todo_id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_view_todos(self):
        """
        Handle viewing all todos.
        """
        try:
            todos = self.todo_service.get_all_todos()
            
            if not todos:
                print("Your todo list is empty.")
                return
            
            print("\nYour Todos:")
            for todo in todos:
                print(f"{todo.id}. {todo}")
        except Exception as e:
            print(f"An error occurred while retrieving todos: {e}")

    def handle_update_todo(self):
        """
        Handle updating a todo.
        """
        try:
            todo_id_str = input("Enter the ID of the todo to update: ").strip()
            todo_id = self.input_handler.validate_todo_id(todo_id_str)
            
            if todo_id is None:
                print("Error: Please enter a valid positive integer for the todo ID.")
                return
            
            # Check if the todo exists
            try:
                current_todo = self.todo_service.get_todo_by_id(todo_id)
            except ValueError:
                print(f"Error: No todo with ID {todo_id} exists.")
                return
            
            new_title = input(f"Enter new title for todo '{current_todo.title}': ").strip()
            
            if not self.input_handler.validate_todo_title(new_title):
                print("Error: Todo title cannot be empty and must be 500 characters or less.")
                return
            
            self.todo_service.update_todo(todo_id, new_title)
            print(f"Todo {todo_id} updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_mark_complete(self):
        """
        Handle marking a todo as completed.
        """
        try:
            todo_id_str = input("Enter the ID of the todo to mark as completed: ").strip()
            todo_id = self.input_handler.validate_todo_id(todo_id_str)
            
            if todo_id is None:
                print("Error: Please enter a valid positive integer for the todo ID.")
                return
            
            # Check if the todo exists
            try:
                current_todo = self.todo_service.get_todo_by_id(todo_id)
            except ValueError:
                print(f"Error: No todo with ID {todo_id} exists.")
                return
            
            self.todo_service.mark_todo_complete(todo_id, True)
            print(f"Todo {todo_id} marked as completed.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def handle_delete_todo(self):
        """
        Handle deleting a todo.
        """
        try:
            todo_id_str = input("Enter the ID of the todo to delete: ").strip()
            todo_id = self.input_handler.validate_todo_id(todo_id_str)
            
            if todo_id is None:
                print("Error: Please enter a valid positive integer for the todo ID.")
                return
            
            # Check if the todo exists
            try:
                current_todo = self.todo_service.get_todo_by_id(todo_id)
            except ValueError:
                print(f"Error: No todo with ID {todo_id} exists.")
                return
            
            confirm = input(f"Are you sure you want to delete todo '{current_todo.title}'? (y/N): ").strip().lower()
            
            if confirm in ['y', 'yes']:
                self.todo_service.delete_todo(todo_id)
                print(f"Todo {todo_id} deleted successfully.")
            else:
                print("Deletion cancelled.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")