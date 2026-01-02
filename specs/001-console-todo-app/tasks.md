# Tasks: Console-Based Todo Application

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/
- [X] T002 [P] Create src/todo/__init__.py
- [X] T003 [P] Create src/ui/__init__.py
- [X] T004 [P] Create tests/unit/__init__.py
- [X] T005 [P] Create tests/integration/__init__.py
- [X] T006 [P] Create tests/contract/__init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T007 Create Todo model in src/todo/model.py with id, title, completed, created_at fields
- [X] T008 Create TodoService in src/todo/service.py with all required operations (add, get all, get by id, update, delete, mark complete)
- [X] T009 Create InputHandler in src/ui/input_handler.py for input validation
- [X] T010 Create Menu in src/ui/menu.py for console interface
- [X] T011 Create main.py entry point that initializes the application
- [X] T012 [P] Create unit tests for Todo model in tests/unit/test_todo_model.py
- [X] T013 [P] Create unit tests for TodoService in tests/unit/test_todo_service.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items to their list

**Independent Test**: Can be fully tested by adding a new todo item and verifying it appears in the list of todos.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T014 [P] [US1] Contract test for add_todo function in tests/contract/test_add_todo.py
- [X] T015 [P] [US1] Integration test for adding todo workflow in tests/integration/test_add_todo_workflow.py

### Implementation for User Story 1

- [X] T016 [US1] Implement add_todo functionality in src/todo/service.py
- [X] T017 [US1] Implement add todo console interface in src/ui/menu.py
- [X] T018 [US1] Connect add todo functionality in main.py
- [X] T019 [US1] Add input validation for add todo in src/ui/input_handler.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Todo Items (Priority: P1)

**Goal**: Enable users to view all their todo items with completion status

**Independent Test**: Can be fully tested by adding some todo items and then viewing the complete list.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T020 [P] [US2] Contract test for get_all_todos function in tests/contract/test_get_all_todos.py
- [X] T021 [P] [US2] Integration test for viewing todos workflow in tests/integration/test_view_todos_workflow.py

### Implementation for User Story 2

- [X] T022 [US2] Implement get_all_todos functionality in src/todo/service.py
- [X] T023 [US2] Implement view todos console interface in src/ui/menu.py
- [X] T024 [US2] Connect view todos functionality in main.py
- [X] T025 [US2] Format output display for todos in src/ui/menu.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo as Completed (Priority: P2)

**Goal**: Enable users to mark a todo item as completed to track progress

**Independent Test**: Can be fully tested by marking a todo item as completed and verifying its status changes.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T026 [P] [US3] Contract test for mark_todo_complete function in tests/contract/test_mark_todo_complete.py
- [X] T027 [P] [US3] Integration test for marking todo complete workflow in tests/integration/test_mark_todo_complete_workflow.py

### Implementation for User Story 3

- [X] T028 [US3] Implement mark_todo_complete functionality in src/todo/service.py
- [X] T029 [US3] Implement mark todo complete console interface in src/ui/menu.py
- [X] T030 [US3] Connect mark todo complete functionality in main.py
- [X] T031 [US3] Add input validation for todo ID in src/ui/input_handler.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Todo Item (Priority: P2)

**Goal**: Enable users to update an existing todo item's description

**Independent Test**: Can be fully tested by updating a todo item and verifying the changes are saved.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T032 [P] [US4] Contract test for update_todo function in tests/contract/test_update_todo.py
- [X] T033 [P] [US4] Integration test for updating todo workflow in tests/integration/test_update_todo_workflow.py

### Implementation for User Story 4

- [X] T034 [US4] Implement update_todo functionality in src/todo/service.py
- [X] T035 [US4] Implement update todo console interface in src/ui/menu.py
- [X] T036 [US4] Connect update todo functionality in main.py
- [X] T037 [US4] Add input validation for update in src/ui/input_handler.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Todo Item (Priority: P3)

**Goal**: Enable users to delete a todo item to remove obsolete tasks

**Independent Test**: Can be fully tested by deleting a todo item and verifying it's removed from the list.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T038 [P] [US5] Contract test for delete_todo function in tests/contract/test_delete_todo.py
- [X] T039 [P] [US5] Integration test for deleting todo workflow in tests/integration/test_delete_todo_workflow.py

### Implementation for User Story 5

- [X] T040 [US5] Implement delete_todo functionality in src/todo/service.py
- [X] T041 [US5] Implement delete todo console interface in src/ui/menu.py
- [X] T042 [US5] Connect delete todo functionality in main.py
- [X] T043 [US5] Add input validation for delete in src/ui/input_handler.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T044 [P] Add error handling for all operations in src/todo/service.py
- [X] T045 [P] Add comprehensive input validation in src/ui/input_handler.py
- [X] T046 [P] Add user-friendly error messages in src/ui/menu.py
- [X] T047 [P] Add documentation strings to all functions in src/todo/ and src/ui/
- [X] T048 [P] Add integration tests in tests/integration/test_ui_integration.py
- [X] T049 [P] Add contract tests in tests/contract/test_api_contract.py
- [X] T050 Run application end-to-end validation using quickstart.md instructions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
- [ ] T014 [P] [US1] Contract test for add_todo function in tests/contract/test_add_todo.py
- [ ] T015 [P] [US1] Integration test for adding todo workflow in tests/integration/test_add_todo_workflow.py

# Launch implementation tasks for User Story 1 together:
- [ ] T016 [US1] Implement add_todo functionality in src/todo/service.py
- [ ] T017 [US1] Implement add todo console interface in src/ui/menu.py
- [ ] T018 [US1] Connect add todo functionality in main.py
- [ ] T019 [US1] Add input validation for add todo in src/ui/input_handler.py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence