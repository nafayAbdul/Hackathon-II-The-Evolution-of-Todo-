from typing import Optional


class InputHandler:
    """
    Handles input validation for the todo application.
    """
    
    @staticmethod
    def validate_todo_title(title: str) -> bool:
        """
        Validate a todo title.
        
        Args:
            title: The title to validate
            
        Returns:
            True if the title is valid, False otherwise
        """
        if not title:
            return False
        if title.strip() == "":
            return False
        if len(title.strip()) > 500:  # Max reasonable length
            return False
        return True

    @staticmethod
    def validate_todo_id(todo_id: str) -> Optional[int]:
        """
        Validate a todo ID.
        
        Args:
            todo_id: The ID to validate (as string from user input)
            
        Returns:
            The integer ID if valid, None otherwise
        """
        try:
            id_int = int(todo_id)
            if id_int <= 0:
                return None
            return id_int
        except ValueError:
            return None

    @staticmethod
    def sanitize_input(input_str: str) -> str:
        """
        Sanitize user input by stripping whitespace.
        
        Args:
            input_str: The input string to sanitize
            
        Returns:
            The sanitized string
        """
        return input_str.strip()