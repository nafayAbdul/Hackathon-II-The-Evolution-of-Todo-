# API Contract: Console-Based Todo Application

## Overview
This document describes the functional contracts for the console-based todo application. Since this is a console application without a traditional API, these contracts represent the functional interfaces between different components.

## Todo Service Interface

### Add Todo
- **Function**: `add_todo(title: str) -> int`
- **Input**: Todo title/description (string)
- **Output**: Unique ID of the newly created todo (integer)
- **Preconditions**: Title is not empty or whitespace-only
- **Postconditions**: New todo exists in the collection with 'completed' = False
- **Error conditions**: 
  - ValueError if title is empty or whitespace-only

### Get All Todos
- **Function**: `get_all_todos() -> List[Todo]`
- **Input**: None
- **Output**: List of all todos in the collection
- **Preconditions**: None
- **Postconditions**: Returns all todos, sorted by ID
- **Error conditions**: None

### Get Todo by ID
- **Function**: `get_todo_by_id(todo_id: int) -> Todo`
- **Input**: Unique todo ID (integer)
- **Output**: Todo object with the specified ID
- **Preconditions**: Todo with given ID exists
- **Postconditions**: Returns the requested todo
- **Error conditions**: 
  - ValueError if todo with ID does not exist

### Update Todo
- **Function**: `update_todo(todo_id: int, new_title: str) -> bool`
- **Input**: Todo ID (integer) and new title (string)
- **Output**: Success status (boolean)
- **Preconditions**: Todo with given ID exists, new title is not empty
- **Postconditions**: Todo title is updated
- **Error conditions**: 
  - ValueError if todo with ID does not exist
  - ValueError if new title is empty

### Mark Todo Complete
- **Function**: `mark_todo_complete(todo_id: int, completed: bool = True) -> bool`
- **Input**: Todo ID (integer), completion status (boolean, default True)
- **Output**: Success status (boolean)
- **Preconditions**: Todo with given ID exists
- **Postconditions**: Todo completion status is updated
- **Error conditions**: 
  - ValueError if todo with ID does not exist

### Delete Todo
- **Function**: `delete_todo(todo_id: int) -> bool`
- **Input**: Todo ID (integer)
- **Output**: Success status (boolean)
- **Preconditions**: Todo with given ID exists
- **Postconditions**: Todo is removed from the collection
- **Error conditions**: 
  - ValueError if todo with ID does not exist

## Todo Model Structure

### Todo Object
- **id**: Unique identifier (integer)
- **title**: Text description (string)
- **completed**: Completion status (boolean)
- **created_at**: Creation timestamp (datetime)

## Console Interface

### Input Validation
- All user inputs must be validated before processing
- Invalid inputs should result in appropriate error messages
- Commands should be validated against the available command set

### Output Format
- Todo lists should display ID, completion status, and title
- Example: `1. [X] Complete project` or `2. [ ] Buy groceries`
- Error messages should be clear and actionable