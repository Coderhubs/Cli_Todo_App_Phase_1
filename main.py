#!/usr/bin/env python3
"""
Elegant Console-based Todo Application

A sophisticated and beautiful Python console todo app with in-memory storage
that allows users to add, view, update, delete, and mark tasks as complete.
Features modern TUI with elegant colors, animations, and interactive navigation.
"""

import os
import sys
import time
import json
from datetime import datetime
from typing import List, Dict, Tuple, Optional


# ANSI color codes for elegant output
class Colors:
    # Header and title colors (rich and vibrant)
    HEADER_BG = '\033[48;5;236m'   # Dark gray background
    HEADER_FG = '\033[38;5;51m'    # Cyan foreground
    TITLE = '\033[38;5;207m'       # Magenta title

    # Menu colors
    MENU_HEADER = '\033[38;5;51m'  # Cyan
    MENU_OPTION = '\033[38;5;248m'  # Muted gray
    MENU_SELECTED = '\033[38;5;231;48;5;69m'  # Light text with blue background

    # Task colors (vibrant and eye-catching)
    TASK_ID = '\033[38;5;255m'        # Bright white for IDs
    TASK_STATUS_ACTIVE = '\033[38;5;226m'   # Yellow for active
    TASK_STATUS_COMPLETED = '\033[38;5;46m' # Green for completed
    TASK_DESCRIPTION = '\033[38;5;248m'    # Muted gray for descriptions
    TASK_TIMESTAMP = '\033[38;5;245m'      # Gray for timestamps

    # Status colors (eye-catching)
    SUCCESS = '\033[38;5;46m'      # Bright green
    WARNING = '\033[38;5;226m'     # Bright yellow
    ERROR = '\033[38;5;196m'       # Bright red
    INFO = '\033[38;5;51m'         # Bright cyan

    # Table and border elements (rounded corners)
    TABLE_BORDER = '\033[38;5;240m'  # Dark gray for table borders
    TABLE_HEADER = '\033[38;5;51m'  # Cyan for table headers

    # Decorative elements
    HIGHLIGHT = '\033[38;5;215m'   # Magenta accent

    # Text styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSE = '\033[7m'
    RESET = '\033[0m'


class Task:
    """Represents a single todo task with id, description, and completion status."""

    def __init__(self, task_id: int, description: str, completed: bool = False, priority: str = "medium", category: str = "General", due_date: str = ""):
        self.id = task_id
        self.description = description
        self.completed = completed
        self.priority = priority  # "high", "medium", "low"
        self.category = category
        self.due_date = due_date
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def __str__(self):
        # Standard string representation for display
        if self.completed:
            status = f"{Colors.TASK_STATUS_COMPLETED}✅{Colors.RESET}"
            id_color = Colors.TASK_STATUS_COMPLETED
            desc_color = Colors.TASK_DESCRIPTION
        else:
            status = f"{Colors.TASK_STATUS_ACTIVE}⭕{Colors.RESET}"
            id_color = Colors.TASK_STATUS_ACTIVE
            desc_color = Colors.TASK_DESCRIPTION

        # Priority indicator
        if self.priority == "high":
            priority_indicator = f"{Colors.ERROR}🔴{Colors.RESET}"
        elif self.priority == "medium":
            priority_indicator = f"{Colors.WARNING}🟡{Colors.RESET}"
        else:  # low
            priority_indicator = f"{Colors.SUCCESS}🟢{Colors.RESET}"

        # Due date indicator if present
        due_indicator = f" ⏰{self.due_date}" if self.due_date else ""

        return f" {status} {priority_indicator} {id_color}[{self.id:2d}]{Colors.RESET} {desc_color}{self.description}{Colors.RESET}{due_indicator}"

    def get_table_row(self):
        """Return task data formatted for table display"""
        if self.completed:
            status = f"{Colors.TASK_STATUS_COMPLETED}✅{Colors.RESET}"
        else:
            status = f"{Colors.TASK_STATUS_ACTIVE}⭕{Colors.RESET}"

        # Priority indicator
        if self.priority == "high":
            priority_indicator = f"{Colors.ERROR}🔴{Colors.RESET}"
        elif self.priority == "medium":
            priority_indicator = f"{Colors.WARNING}🟡{Colors.RESET}"
        else:  # low
            priority_indicator = f"{Colors.SUCCESS}🟢{Colors.RESET}"

        timestamp_color = Colors.TASK_TIMESTAMP
        due_date_display = f"{self.due_date}" if self.due_date else "None"
        return f"{self.id:2d}", status, priority_indicator, self.description, f"{timestamp_color}{self.created_at}{Colors.RESET}", f"{due_date_display}", self.category

    def to_dict(self) -> Dict:
        """Convert task to dictionary representation."""
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "priority": self.priority,
            "category": self.category,
            "due_date": self.due_date,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Create a Task instance from a dictionary."""
        task = cls(
            data["id"],
            data["description"],
            data["completed"],
            data.get("priority", "medium"),
            data.get("category", "General"),
            data.get("due_date", "")
        )
        if "created_at" in data:
            task.created_at = data["created_at"]
        else:
            # Fallback to current time if no timestamp exists
            task.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        return task


class TaskManager:
    """Manages the task storage with JSON persistence and operations."""

    def __init__(self, storage_file: str = "tasks.json"):
        self.storage_file = storage_file
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load_from_json()

    def add_task(self, description: str, priority: str = "medium", category: str = "General", due_date: str = "") -> bool:
        """Add a new task to the task list. Returns True if successful."""
        if not self._validate_task_description(description)[0]:
            return False

        task = Task(self.next_id, description.strip(), priority=priority, category=category, due_date=due_date)
        self.tasks.append(task)
        self.next_id += 1
        self.save_to_json()
        return True

    def view_tasks(self) -> List[Task]:
        """Return all tasks in the task list."""
        return self.tasks

    def update_task(self, task_id: int, new_description: str, priority: str = "medium", category: str = "General", due_date: str = "") -> bool:
        """Update task details by ID. Returns True if successful."""
        if not self._validate_task_id(task_id)[0]:
            return False

        if not self._validate_task_description(new_description)[0]:
            return False

        task = self._get_task_by_id(task_id)
        if task:
            task.description = new_description.strip()
            task.priority = priority
            task.category = category
            task.due_date = due_date
            self.save_to_json()
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete task by ID. Returns True if successful."""
        if not self._validate_task_id(task_id)[0]:
            return False

        task = self._get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            # Renumber remaining tasks to maintain sequential IDs
            self._renumber_tasks()
            self.save_to_json()
            return True
        return False

    def mark_task_complete(self, task_id: int) -> bool:
        """Toggle task completion status by ID. Returns True if successful."""
        if not self._validate_task_id(task_id)[0]:
            return False

        task = self._get_task_by_id(task_id)
        if task:
            task.completed = not task.completed
            self.save_to_json()
            return True
        return False

    def _get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Find and return a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def _validate_task_description(self, description: str) -> Tuple[bool, str]:
        """Validate task description. Returns (is_valid, error_message)."""
        if not description or not description.strip():
            return False, "Task description cannot be empty"

        if len(description) > 500:
            return False, "Task description is too long (max 500 characters)"

        return True, ""

    def _validate_task_id(self, task_id: int) -> Tuple[bool, str]:
        """Validate task ID exists in task list. Returns (is_valid, error_message)."""
        if task_id < 1:
            return False, "Task ID must be a positive integer"

        if not any(task.id == task_id for task in self.tasks):
            return False, f"Task with ID {task_id} does not exist"

        return True, ""

    def _validate_priority(self, priority: str) -> Tuple[bool, str]:
        """Validate task priority. Returns (is_valid, error_message)."""
        valid_priorities = ["high", "medium", "low"]
        if priority not in valid_priorities:
            return False, f"Priority must be one of: {', '.join(valid_priorities)}"

        return True, ""

    def _renumber_tasks(self):
        """Renumber tasks to maintain sequential IDs after deletion."""
        for i, task in enumerate(self.tasks, 1):
            task.id = i
        self.next_id = len(self.tasks) + 1

    def save_to_json(self):
        """Save tasks to a JSON file."""
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                tasks_data = [task.to_dict() for task in self.tasks]
                json.dump({
                    "tasks": tasks_data,
                    "next_id": self.next_id
                }, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving tasks to JSON: {e}")

    def load_from_json(self):
        """Load tasks from a JSON file."""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                    self.tasks = []
                    for task_data in data.get("tasks", []):
                        task = Task.from_dict(task_data)
                        self.tasks.append(task)

                    self.next_id = data.get("next_id", 1)
            else:
                # Initialize with empty list if file doesn't exist
                self.tasks = []
                self.next_id = 1
                self.save_to_json()
        except (json.JSONDecodeError, KeyError, FileNotFoundError):
            # If there's an error loading, start fresh
            self.tasks = []
            self.next_id = 1
            self.save_to_json()


class UIHelper:
    """Handles elegant UI formatting and display functions."""

    @staticmethod
    def clear_screen():
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_header():
        """Display the stylish application header with gradient effect."""
        print(f"{Colors.HEADER_BG}{Colors.BOLD}╔════════════════════════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.HEADER_BG}{Colors.BOLD}║{Colors.RESET}  {Colors.TITLE}{Colors.BOLD}🌟 PYTHON TODO MANAGER 🌟{Colors.RESET}                                           {Colors.HEADER_BG}{Colors.BOLD}║{Colors.RESET}")
        print(f"{Colors.HEADER_BG}{Colors.BOLD}║{Colors.RESET}  {Colors.INFO}Efficient task management at your fingertips{Colors.RESET}                         {Colors.HEADER_BG}{Colors.BOLD}║{Colors.RESET}")
        print(f"{Colors.HEADER_BG}{Colors.BOLD}║{Colors.RESET}  {Colors.INFO}Organize, prioritize, and accomplish your goals{Colors.RESET}                        {Colors.HEADER_BG}{Colors.BOLD}║{Colors.RESET}")
        print(f"{Colors.HEADER_BG}{Colors.BOLD}╚════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}")
        print()

    @staticmethod
    def display_menu(selected_option: int = 0):
        """Display the main menu options with clean, professional highlighting."""
        options = [
            f"{Colors.MENU_OPTION}1.{Colors.RESET} {Colors.HIGHLIGHT}📝 Add New Task{Colors.RESET}",
            f"{Colors.MENU_OPTION}2.{Colors.RESET} {Colors.HIGHLIGHT}👀 View All Tasks{Colors.RESET}",
            f"{Colors.MENU_OPTION}3.{Colors.RESET} {Colors.HIGHLIGHT}✏️  Update Task{Colors.RESET}",
            f"{Colors.MENU_OPTION}4.{Colors.RESET} {Colors.HIGHLIGHT}🗑️  Delete Task{Colors.RESET}",
            f"{Colors.MENU_OPTION}5.{Colors.RESET} {Colors.HIGHLIGHT}✅ Toggle Complete{Colors.RESET}",
            f"{Colors.MENU_OPTION}6.{Colors.RESET} {Colors.HIGHLIGHT}📊 Statistics{Colors.RESET}",
            f"{Colors.MENU_OPTION}7.{Colors.RESET} {Colors.HIGHLIGHT}🚪 Exit Application{Colors.RESET}"
        ]

        print(f"{Colors.MENU_HEADER}{Colors.BOLD}📋 MAIN MENU:{Colors.RESET}")
        print(f"{Colors.TABLE_BORDER}┌─────────────────────────────────────────────────────────────────────────┐{Colors.RESET}")
        for i, option in enumerate(options):
            if i == selected_option:
                print(f"{Colors.TABLE_BORDER}│{Colors.RESET}  {Colors.MENU_SELECTED}▶ {option}{Colors.RESET}  {Colors.TABLE_BORDER}│{Colors.RESET}")
            else:
                print(f"{Colors.TABLE_BORDER}│{Colors.RESET}    {option}    {Colors.TABLE_BORDER}│{Colors.RESET}")
        print(f"{Colors.TABLE_BORDER}├─────────────────────────────────────────────────────────────────────────┤{Colors.RESET}")
        print(f"{Colors.TABLE_BORDER}│{Colors.INFO} Use ↑ ↓ arrows to navigate, ↵ Enter to select, Ctrl+C to exit   {Colors.TABLE_BORDER}│{Colors.RESET}")
        print(f"{Colors.TABLE_BORDER}└─────────────────────────────────────────────────────────────────────────┘{Colors.RESET}")
        print()

    @staticmethod
    def display_tasks(tasks: List[Task]):
        """Display all tasks in a comprehensive table format with all attributes."""
        if not tasks:
            print(f"{Colors.WARNING}🤖 No tasks found. Start adding tasks to begin!{Colors.RESET}")
            return

        print(f"{Colors.TABLE_HEADER}{Colors.BOLD}📋 TASK LIST ({len(tasks)} items):{Colors.RESET}")

        # Print table header
        print(f"{Colors.TABLE_BORDER}┌─────┬──────┬──────┬─────────────────────────┬──────────────────┬─────────────┬─────────────────┐{Colors.RESET}")
        print(f"{Colors.TABLE_BORDER}│{Colors.TABLE_HEADER} ID  {Colors.TABLE_BORDER}│{Colors.TABLE_HEADER} STAT {Colors.TABLE_BORDER}│{Colors.TABLE_HEADER} PRIO {Colors.TABLE_BORDER}│{Colors.TABLE_HEADER} DESCRIPTION         {Colors.TABLE_BORDER}│{Colors.TABLE_HEADER} CREATED AT    {Colors.TABLE_BORDER}│{Colors.TABLE_HEADER} DUE DATE  {Colors.TABLE_BORDER}│{Colors.TABLE_HEADER} CATEGORY      {Colors.TABLE_BORDER}│{Colors.RESET}")
        print(f"{Colors.TABLE_BORDER}├─────┼──────┼──────┼─────────────────────────┼──────────────────┼─────────────┼─────────────────┤{Colors.RESET}")

        # Print each task as a row in the table
        for task in tasks:
            task_id, status, priority, description, timestamp, due_date, category = task.get_table_row()
            # Truncate description if too long
            if len(description) > 23:
                description = description[:20] + "..."
            # Truncate category if too long
            if len(category) > 13:
                category = category[:10] + "..."
            print(f"{Colors.TABLE_BORDER}│{Colors.RESET} {task_id:>2s}  {Colors.TABLE_BORDER}│{Colors.RESET} {status}  {Colors.TABLE_BORDER}│{Colors.RESET} {priority}  {Colors.TABLE_BORDER}│{Colors.RESET} {description:<23s} {Colors.TABLE_BORDER}│{Colors.RESET} {timestamp:<16s} {Colors.TABLE_BORDER}│{Colors.RESET} {due_date:<9s} {Colors.TABLE_BORDER}│{Colors.RESET} {category:<13s} {Colors.TABLE_BORDER}│{Colors.RESET}")

        # Print table footer
        print(f"{Colors.TABLE_BORDER}└─────┴──────┴──────┴─────────────────────────┴──────────────────┴─────────────┴─────────────────┘{Colors.RESET}")
        print()

    @staticmethod
    def display_message(message: str):
        """Display an AI-inspired success message to the user."""
        print(f"\n{Colors.SUCCESS}🤖 {message} 🤖{Colors.RESET}\n")

    @staticmethod
    def display_error(error_message: str):
        """Display an AI-inspired error message to the user."""
        print(f"\n{Colors.ERROR}⚠️  ERROR: {error_message} ⚠️{Colors.RESET}\n")


class InteractiveMenuHandler:
    """Handles elegant interactive menu navigation with arrow keys."""

    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager
        self.ui = UIHelper()
        self.options = [
            "1. Add Task",
            "2. View Tasks",
            "3. Update Task",
            "4. Delete Task",
            "5. Mark Task as Complete",
            "6. Statistics",
            "7. Exit"
        ]

    def get_key(self):
        """Get a single keypress from user without pressing Enter."""
        try:
            # Windows
            import msvcrt
            key = msvcrt.getch()
            if key in [b'\x00', b'\xe0']:  # Special key prefix on Windows
                key = msvcrt.getch()
                if key == b'H':
                    return 'UP'
                elif key == b'P':
                    return 'DOWN'
            elif key in [b'\r', b'\n']:  # Enter key
                return 'ENTER'
            return key.decode('utf-8', errors='ignore')
        except ImportError:
            # Unix/Linux/MacOS
            import tty
            import termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                char = sys.stdin.read(1)
                if char == '\x1b':  # ESC sequence
                    char += sys.stdin.read(2)  # Read next 2 chars for arrow keys
                    if char == '\x1b[A':
                        return 'UP'
                    elif char == '\x1b[B':
                        return 'DOWN'
                elif char in ['\n', '\r']:  # Enter key
                    return 'ENTER'
                return char
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def run_interactive_menu(self):
        """Run the main application loop with interactive menu."""
        selected_index = 0

        while True:
            # Handle continuous navigation
            while True:
                self.ui.clear_screen()
                self.ui.display_header()
                self.ui.display_tasks(self.task_manager.view_tasks())
                self.ui.display_menu(selected_index)

                key = self.get_key()

                if key == 'UP':  # Up arrow
                    selected_index = max(0, selected_index - 1)
                elif key == 'DOWN':  # Down arrow
                    selected_index = min(len(self.options) - 1, selected_index + 1)
                elif key == 'ENTER':  # Enter key
                    break  # Exit the navigation loop to execute the selection
                elif key.lower() == 'q':  # Quick exit with 'q'
                    return  # Exit the function entirely

            # Execute the selected option
            if selected_index == 0:  # Add Task
                self._handle_add_task()
            elif selected_index == 1:  # View Tasks
                self._handle_view_tasks()
            elif selected_index == 2:  # Update Task
                self._handle_update_task()
            elif selected_index == 3:  # Delete Task
                self._handle_delete_task()
            elif selected_index == 4:  # Mark Task as Complete
                self._handle_mark_task_complete()
            elif selected_index == 5:  # Statistics
                self._handle_statistics()
            elif selected_index == 6:  # Exit
                self.ui.display_message("Thank you for using the Python Todo Manager! 🚀")
                break  # Exit the main loop

    def _handle_add_task(self):
        """Handle the add task operation."""
        self.ui.clear_screen()
        self.ui.display_header()
        self.ui.display_tasks(self.task_manager.view_tasks())

        print(f"\n{Colors.HIGHLIGHT}{Colors.BOLD}📝 CREATE NEW TASK{Colors.RESET}")
        description = input(f"{Colors.INFO}📝 Enter task description: {Colors.RESET}").strip()

        # Get priority
        print(f"{Colors.INFO}Select priority:{Colors.RESET}")
        print(f"  1. 🔴 High")
        print(f"  2. 🟡 Medium (default)")
        print(f"  3. 🟢 Low")
        priority_choice = input(f"{Colors.INFO}Enter choice (1-3, default 2): {Colors.RESET}").strip()
        priority_map = {"1": "high", "2": "medium", "3": "low"}
        priority = priority_map.get(priority_choice, "medium")

        # Get category
        category = input(f"{Colors.INFO}🏷️  Enter category (optional, default 'General'): {Colors.RESET}").strip()
        if not category:
            category = "General"

        # Get due date
        due_date = input(f"{Colors.INFO}⏰ Enter due date (optional, format: YYYY-MM-DD): {Colors.RESET}").strip()

        if self.task_manager.add_task(description, priority=priority, category=category, due_date=due_date):
            self.ui.display_message("Task created successfully! ✨")
        else:
            _, error_msg = self.task_manager._validate_task_description(description)
            self.ui.display_error(error_msg)

        input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")

    def _handle_view_tasks(self):
        """Handle the view tasks operation."""
        tasks = self.task_manager.view_tasks()
        self.ui.clear_screen()
        self.ui.display_header()
        self.ui.display_tasks(tasks)
        input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")

    def _handle_update_task(self):
        """Handle the update task operation."""
        tasks = self.task_manager.view_tasks()
        if not tasks:
            self.ui.clear_screen()
            self.ui.display_header()
            self.ui.display_error("No tasks available to update.")
            input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")
            return

        self.ui.clear_screen()
        self.ui.display_header()
        self.ui.display_tasks(tasks)

        try:
            task_id_str = input(f"{Colors.INFO}🔢 Enter task ID to update: {Colors.RESET}").strip()
            if not task_id_str:
                input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")
                return
            task_id = int(task_id_str)
            task = self.task_manager._get_task_by_id(task_id)
            if not task:
                self.ui.display_error(f"Task with ID {task_id} does not exist.")
                input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")
                return

            print(f"{Colors.INFO}Current task: {task.description}{Colors.RESET}")
            new_description = input(f"{Colors.INFO}✏️  Enter new description (leave blank to keep current): {Colors.RESET}").strip()
            if not new_description:
                new_description = task.description

            # Update priority if needed
            print(f"{Colors.INFO}Current priority: {task.priority}{Colors.RESET}")
            print(f"  1. 🔴 High")
            print(f"  2. 🟡 Medium")
            print(f"  3. 🟢 Low")
            priority_choice = input(f"{Colors.INFO}Enter new priority (1-3, leave blank to keep current): {Colors.RESET}").strip()
            priority_map = {"1": "high", "2": "medium", "3": "low"}
            priority = priority_map.get(priority_choice, task.priority)

            # Update category if needed
            new_category = input(f"{Colors.INFO}🏷️  Enter new category (leave blank to keep '{task.category}'): {Colors.RESET}").strip()
            if not new_category:
                new_category = task.category

            # Update due date if needed
            new_due_date = input(f"{Colors.INFO}⏰ Enter new due date (YYYY-MM-DD, leave blank to keep current): {Colors.RESET}").strip()
            if not new_due_date:
                new_due_date = task.due_date

            if self.task_manager.update_task(task_id, new_description, priority=priority, category=new_category, due_date=new_due_date):
                self.ui.display_message("Task updated successfully! 🔄")
            else:
                _, error_msg = self.task_manager._validate_task_description(new_description)
                self.ui.display_error(error_msg)
        except ValueError:
            self.ui.display_error("Invalid task ID. Please enter a number.")
        except KeyboardInterrupt:
            pass
        finally:
            input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")

    def _handle_delete_task(self):
        """Handle the delete task operation."""
        tasks = self.task_manager.view_tasks()
        if not tasks:
            self.ui.clear_screen()
            self.ui.display_header()
            self.ui.display_error("No tasks available to delete.")
            input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")
            return

        self.ui.clear_screen()
        self.ui.display_header()
        self.ui.display_tasks(tasks)

        try:
            task_id_str = input(f"{Colors.INFO}🔢 Enter task ID to delete: {Colors.RESET}").strip()
            if not task_id_str:
                input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")
                return
            task_id = int(task_id_str)

            # Confirmation
            task = self.task_manager._get_task_by_id(task_id)
            if task:
                print(f"{Colors.WARNING}⚠️  You are about to delete task: {task.description}{Colors.RESET}")
                confirm = input(f"{Colors.WARNING}Type 'DELETE' to confirm: {Colors.RESET}").strip()
                if confirm.upper() != "DELETE":
                    self.ui.display_message("Deletion cancelled.")
                    input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")
                    return

            if self.task_manager.delete_task(task_id):
                self.ui.display_message("Task removed successfully! 🗑️")
            else:
                _, error_msg = self.task_manager._validate_task_id(task_id)
                self.ui.display_error(error_msg)
        except ValueError:
            self.ui.display_error("Invalid task ID. Please enter a number.")
        except KeyboardInterrupt:
            pass
        finally:
            input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")

    def _handle_mark_task_complete(self):
        """Handle the mark task complete operation."""
        tasks = self.task_manager.view_tasks()
        if not tasks:
            self.ui.clear_screen()
            self.ui.display_header()
            self.ui.display_error("No tasks available to toggle.")
            input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")
            return

        self.ui.clear_screen()
        self.ui.display_header()
        self.ui.display_tasks(tasks)

        try:
            task_id_str = input(f"{Colors.INFO}🔢 Enter task ID to toggle completion: {Colors.RESET}").strip()
            if not task_id_str:
                input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")
                return
            task_id = int(task_id_str)

            if self.task_manager.mark_task_complete(task_id):
                task = self.task_manager._get_task_by_id(task_id)
                status = "completed" if task.completed else "marked as incomplete"
                self.ui.display_message(f"Task {status}! {('✅' if task.completed else '⭕')}")
            else:
                _, error_msg = self.task_manager._validate_task_id(task_id)
                self.ui.display_error(error_msg)
        except ValueError:
            self.ui.display_error("Invalid task ID. Please enter a number.")
        except KeyboardInterrupt:
            pass
        finally:
            input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")

    def _handle_statistics(self):
        """Handle the statistics display operation."""
        tasks = self.task_manager.view_tasks()
        self.ui.clear_screen()
        self.ui.display_header()

        if not tasks:
            print(f"{Colors.WARNING}📊 No tasks to analyze.{Colors.RESET}")
        else:
            # Calculate statistics
            total_tasks = len(tasks)
            completed_tasks = sum(1 for task in tasks if task.completed)
            pending_tasks = total_tasks - completed_tasks

            high_priority = sum(1 for task in tasks if task.priority == "high" and not task.completed)
            medium_priority = sum(1 for task in tasks if task.priority == "medium" and not task.completed)
            low_priority = sum(1 for task in tasks if task.priority == "low" and not task.completed)

            # Display statistics
            print(f"{Colors.MENU_HEADER}{Colors.BOLD}📊 TASK STATISTICS:{Colors.RESET}")
            print(f"{Colors.TABLE_BORDER}┌─────────────────────────────────────────────────────────┐{Colors.RESET}")
            print(f"{Colors.TABLE_BORDER}│{Colors.RESET} Total Tasks: {total_tasks:<43} {Colors.TABLE_BORDER}│{Colors.RESET}")
            print(f"{Colors.TABLE_BORDER}│{Colors.RESET} Completed:   {completed_tasks:<43} {Colors.TABLE_BORDER}│{Colors.RESET}")
            print(f"{Colors.TABLE_BORDER}│{Colors.RESET} Pending:     {pending_tasks:<43} {Colors.TABLE_BORDER}│{Colors.RESET}")
            print(f"{Colors.TABLE_BORDER}├─────────────────────────────────────────────────────────┤{Colors.RESET}")
            print(f"{Colors.TABLE_BORDER}│{Colors.RESET} Priority - High: {high_priority:<38} {Colors.TABLE_BORDER}│{Colors.RESET}")
            print(f"{Colors.TABLE_BORDER}│{Colors.RESET} Priority - Medium: {medium_priority:<36} {Colors.TABLE_BORDER}│{Colors.RESET}")
            print(f"{Colors.TABLE_BORDER}│{Colors.RESET} Priority - Low: {low_priority:<37} {Colors.TABLE_BORDER}│{Colors.RESET}")
            print(f"{Colors.TABLE_BORDER}└─────────────────────────────────────────────────────────┘{Colors.RESET}")

        input(f"\n{Colors.INFO}Press ↵ Enter to return to menu...{Colors.RESET}")


def main():
    """Main application entry point."""
    task_manager = TaskManager(storage_file="tasks.json")
    menu_handler = InteractiveMenuHandler(task_manager)

    try:
        print(f"{Colors.INFO}🚀 Launching Python Todo Manager with JSON storage...{Colors.RESET}")
        time.sleep(0.5)  # Brief animation effect
        menu_handler.run_interactive_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}👋 Application interrupted. Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}⚠️  System error: {e}{Colors.RESET}")
        print(f"{Colors.ERROR}🔄 Please restart the application.{Colors.RESET}")


if __name__ == "__main__":
    main()