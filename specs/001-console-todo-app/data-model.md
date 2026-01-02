# Data Model: Console-Based Todo Application

## Todo Entity

### Fields
- **id**: Unique identifier (integer, auto-generated, runtime-only)
- **title**: Text description of the todo item (string, required)
- **completed**: Completion status (boolean, default: False)
- **created_at**: Timestamp when todo was created (datetime, auto-generated)

### Validation Rules
- Title must not be empty or contain only whitespace
- ID must be unique within the application session
- Title length should be reasonable (e.g., max 500 characters)

### State Transitions
- New todo: `completed = False`
- When marked complete: `completed = True`
- When marked incomplete: `completed = False` (if previously completed)

## Todo Collection

### Structure
- In-memory storage using Python list or dictionary
- If using dictionary: key = id, value = todo object
- If using list: index not used as ID since items can be deleted

### Operations
- Add: Insert new todo with unique ID
- Get All: Return all todos
- Get by ID: Return specific todo
- Update: Modify existing todo properties
- Delete: Remove todo by ID
- Mark Complete: Update completion status