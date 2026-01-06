#!/usr/bin/env python3
"""
Test script to verify the Todo App functionality
"""

from main import TaskManager, Task

def test_basic_functionality():
    print("Testing basic functionality of the Todo App...")

    # Create a task manager
    tm = TaskManager()

    # Test adding tasks
    print("\n1. Testing add_task functionality:")
    result = tm.add_task("Test task 1")
    print(f"   Added 'Test task 1': {result}")
    print(f"   Number of tasks: {len(tm.view_tasks())}")

    result = tm.add_task("Test task 2")
    print(f"   Added 'Test task 2': {result}")
    print(f"   Number of tasks: {len(tm.view_tasks())}")

    # Test viewing tasks
    print("\n2. Testing view_tasks functionality:")
    tasks = tm.view_tasks()
    for task in tasks:
        print(f"   Task: {task}")

    # Test marking task as complete
    print("\n3. Testing mark_task_complete functionality:")
    result = tm.mark_task_complete(1)
    print(f"   Marked task 1 as complete: {result}")
    tasks = tm.view_tasks()
    for task in tasks:
        print(f"   Task: {task}")

    # Test updating task
    print("\n4. Testing update_task functionality:")
    result = tm.update_task(2, "Updated test task 2")
    print(f"   Updated task 2: {result}")
    tasks = tm.view_tasks()
    for task in tasks:
        print(f"   Task: {task}")

    # Test deleting task
    print("\n5. Testing delete_task functionality:")
    result = tm.delete_task(1)
    print(f"   Deleted task 1: {result}")
    print(f"   Number of tasks: {len(tm.view_tasks())}")
    tasks = tm.view_tasks()
    for task in tasks:
        print(f"   Task: {task}")

    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    test_basic_functionality()