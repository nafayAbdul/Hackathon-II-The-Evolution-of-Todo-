from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Todo:
    """
    Represents a todo item with id, title, completion status, and creation timestamp.
    """
    id: int
    title: str
    completed: bool = False
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def __str__(self) -> str:
        """
        String representation of the todo item.
        Format: [X] or [ ] followed by the title
        """
        status = "X" if self.completed else " "
        return f"[{status}] {self.title}"