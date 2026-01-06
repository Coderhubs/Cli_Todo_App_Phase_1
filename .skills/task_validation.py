# Reusable Skill: Task Validation
# Validates task inputs for the Todo App

def validate_task_description(description: str) -> bool:
    """
    Check if task description is valid (non-empty, max 100 chars).
    """
    if not description or len(description) > 100:
        return False
    return True

def check_duplicate_task(tasks: list, description: str) -> bool:
    """
    Check if a task with the same description already exists.
    tasks: list of dicts [{'id': int, 'description': str, 'complete': bool}]
    """
    for task in tasks:
        if task['description'].lower() == description.lower():
            return True
    return False

# Example usage (for testing)
if __name__ == "__main__":
    tasks = [{'id': 1, 'description': 'Buy milk', 'complete': False}]
    print(validate_task_description("New task"))  # True
    print(check_duplicate_task(tasks, "buy milk"))  # True