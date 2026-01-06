# Reusable Skill: In-Memory Data Storage
# Handles CRUD operations for Todo tasks using a list of dicts

tasks = []  # Global storage: [{'id': int, 'description': str, 'completed': bool}]

def add_task(description: str) -> int:
    """
    Add a new task and return its ID.
    """
    task_id = len(tasks) + 1
    tasks.append({'id': task_id, 'description': description, 'completed': False})
    return task_id

def delete_task(task_id: int) -> bool:
    """
    Delete task by ID. Return True if deleted.
    """
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            return True
    return False

def update_task(task_id: int, new_description: str) -> bool:
    """
    Update task description by ID. Return True if updated.
    """
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            return True
    return False

def mark_complete(task_id: int) -> bool:
    """
    Mark task as completed by ID. Return True if marked.
    """
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return True
    return False

def view_tasks() -> list:
    """
    Return all tasks.
    """
    return tasks

# Example usage (for testing)
if __name__ == "__main__":
    add_task("Buy groceries")
    add_task("Walk dog")
    print(view_tasks())  # Shows list of tasks
    mark_complete(1)
    print(view_tasks())  # Shows updated list