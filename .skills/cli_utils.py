# Reusable Skill: CLI Utilities
# Handles console input/output for the Todo App

import sys

def display_menu():
    """
    Display the main menu options.
    """
    print("\n" + "=" * 40)
    print("     Todo App Console Menu")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Exit")
    print("=" * 40)

def get_user_choice() -> int:
    """
    Get user's choice from menu (1-6).
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice! Please enter 1-6.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_task_description() -> str:
    """
    Get task description from user.
    """
    description = input("Enter task description: ").strip()
    return description

def get_task_id() -> int:
    """
    Get task ID from user.
    """
    while True:
        try:
            task_id = int(input("Enter task ID: "))
            return task_id
        except ValueError:
            print("Invalid ID! Please enter a number.")

def display_tasks(tasks: list):
    """
    Display all tasks in a nice format.
    """
    if not tasks:
        print("No tasks yet!")
        return
    print("\nCurrent Tasks:")
    print("-" * 50)
    for task in tasks:
        status = "✔" if task['completed'] else " "
        print(f"{task['id']}. [{status}] {task['description']}")
    print("-" * 50)

# Example usage (for testing)
if __name__ == "__main__":
    display_menu()
    choice = get_user_choice()
    print(f"You chose: {choice}")
    if choice == 1:
        desc = get_task_description()
        print(f"Task added: {desc}")
    display_tasks([{'id': 1, 'description': 'Test task', 'completed': True}])