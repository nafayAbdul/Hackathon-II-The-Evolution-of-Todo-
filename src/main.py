import sys
import os
# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from todo.service import TodoService
from ui.menu import Menu


def main():
    """
    Main entry point for the todo application.
    """
    print("Starting the Todo Application...")

    # Initialize the service and UI components
    todo_service = TodoService()
    menu = Menu(todo_service)

    while True:
        menu.display_menu()

        try:
            choice = input("\nChoose an option (1-6): ").strip()

            if choice == '1':
                menu.handle_add_todo()
            elif choice == '2':
                menu.handle_view_todos()
            elif choice == '3':
                menu.handle_update_todo()
            elif choice == '4':
                menu.handle_mark_complete()
            elif choice == '5':
                menu.handle_delete_todo()
            elif choice == '6':
                print("Thank you for using the Todo Application. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 6.")
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()