---
description: "Task list for Python Console Todo App implementation"
---

# Tasks: Python Console Todo App

**Input**: Design documents from `/specs/todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Project structure**: main.py at root, src/ for modules
- Paths shown below follow the planned structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are based on the implementation plan for the
  Python Console Todo App.

  Tasks are organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Create main.py entry point file
- [X] T003 [P] Create src/models/ directory and __init__.py
- [X] T004 [P] Create src/services/ directory and __init__.py
- [X] T005 [P] Create src/cli/ directory and __init__.py

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Create Task model in src/models/task.py with id, description, completed fields
- [X] T007 Create in-memory storage in src/services/data_storage.py
- [X] T008 Create validation functions in src/services/validation.py
- [X] T009 Create basic menu display in src/cli/menu.py
- [X] T010 Create UI formatting functions in src/cli/ui.py
- [X] T011 Create main menu loop structure in main.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---
## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks to their todo list

**Independent Test**: User can input a task description and see it appear in their task list.

### Implementation for User Story 1

- [X] T012 Implement add_task function in src/services/task_service.py
- [X] T013 Implement add task menu option in src/cli/menu.py
- [X] T014 Integrate add task functionality in main.py menu loop
- [X] T015 Test adding tasks with valid descriptions
- [X] T016 Test adding tasks with invalid (empty) descriptions

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Allow users to see all their tasks with their completion status

**Independent Test**: User can view all tasks in a clean, formatted list with completion status.

### Implementation for User Story 2

- [X] T017 Implement view_tasks function in src/services/task_service.py
- [X] T018 Implement view tasks menu option in src/cli/menu.py
- [X] T019 Create formatted task display in src/cli/ui.py
- [X] T020 Integrate view tasks functionality in main.py menu loop
- [X] T021 Test viewing tasks when list is not empty
- [X] T022 Test viewing tasks when list is empty

**Checkpoint**: User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 5 - Mark Tasks as Complete (Priority: P1)

**Goal**: Allow users to mark tasks as complete to track their progress

**Independent Test**: User can select a task by ID and toggle its completion status.

### Implementation for User Story 5

- [X] T023 Implement mark_task_complete function in src/services/task_service.py
- [X] T024 Implement mark complete menu option in src/cli/menu.py
- [X] T025 Integrate mark complete functionality in main.py menu loop
- [X] T026 Test marking existing tasks as complete
- [X] T027 Test marking completed tasks as incomplete
- [X] T028 Test attempting to mark non-existent tasks

**Checkpoint**: User Stories 1, 2, and 5 should all work independently

---
## Phase 6: User Story 3 - Update Task Description (Priority: P2)

**Goal**: Allow users to modify existing task descriptions

**Independent Test**: User can select a task by ID and update its description.

### Implementation for User Story 3

- [X] T029 Implement update_task function in src/services/task_service.py
- [X] T030 Implement update task menu option in src/cli/menu.py
- [X] T031 Integrate update task functionality in main.py menu loop
- [X] T032 Test updating existing task descriptions
- [X] T033 Test attempting to update non-existent tasks

**Checkpoint**: User Stories 1, 2, 5, and 3 should all work independently

---
## Phase 7: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Allow users to remove completed or unwanted tasks

**Independent Test**: User can select a task by ID and remove it from the list.

### Implementation for User Story 4

- [X] T034 Implement delete_task function in src/services/task_service.py
- [X] T035 Implement delete task menu option in src/cli/menu.py
- [X] T036 Integrate delete task functionality in main.py menu loop
- [X] T037 Test deleting existing tasks
- [X] T038 Test attempting to delete non-existent tasks

**Checkpoint**: All user stories should now be independently functional

---
## Phase 8: Error Handling and Validation

**Purpose**: Comprehensive error handling and validation across all features

- [X] T039 Implement comprehensive input validation across all functions
- [X] T040 Add error handling for invalid menu choices
- [X] T041 Add error handling for invalid task IDs
- [X] T042 Add error handling for empty task descriptions
- [X] T043 Create consistent error message formatting in src/cli/ui.py

---
## Phase 9: Edge Cases and Polish

**Purpose**: Handle edge cases and refine user experience

- [X] T044 Handle empty task list in all operations
- [X] T045 Handle maximum description length (500 chars)
- [X] T046 Handle special characters in task descriptions
- [X] T047 Implement proper task ID management after deletions
- [X] T048 Refine menu display formatting
- [X] T049 Test all error scenarios gracefully
- [X] T050 Final integration testing of all features

---
## Phase 10: Final Integration and Testing

**Purpose**: Complete integration and validation of the entire application

- [X] T051 Integrate all components in main.py
- [X] T052 Test complete user workflow scenarios
- [X] T053 Validate all features work together
- [X] T054 Verify compliance with original specifications
- [X] T055 Final code cleanup and documentation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in priority order (P1 → P2)
- **Error Handling (Phase 8)**: Depends on all user stories being implemented
- **Edge Cases (Phase 9)**: Depends on core functionality
- **Final Integration (Phase 10)**: Depends on all previous phases

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before CLI integration
- Core implementation before error handling
- Story complete before moving to next priority