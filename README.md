![61e69cc6-9936-425a-8568-e4071e5b5c82](https://github.com/user-attachments/assets/9611cb3c-a1ea-4055-b7ec-d0109fa13cd2)
# Python Console Todo App

A sophisticated and beautiful Python console todo application with in-memory storage that allows users to add, view, update, delete, and mark tasks as complete. Features modern TUI with elegant colors, animations, and interactive navigation.

## ✨ Features

### 🎯 **Rich UI & Visual Design**
- Beautiful color scheme with vibrant ANSI colors (cyan, magenta, green, yellow)
- Professional table format with rounded corners using box-drawing characters
- Gradient and stylized text effects in the header
- Clear visual hierarchy and organized panels
- Responsive design with proper spacing and alignment

### 📊 **Task Management**
- **Add Tasks**: Create new tasks with descriptions
- **View Tasks**: Display all tasks in a comprehensive table format
- **Update Tasks**: Modify existing task details
- **Delete Tasks**: Remove tasks with confirmation dialog
- **Mark Complete**: Toggle task completion status
- **Statistics**: View task analytics and breakdowns

### 🎨 **Status & Priority Indicators**
- ✅ **Completed tasks** (green color)
- ⭕ **Pending tasks** (yellow color)
- 🔴 **High priority** (red indicator)
- 🟡 **Medium priority** (yellow indicator)
- 🟢 **Low priority** (green indicator)
- ⏰ **Due date indicator**
- 🏷️ **Category/tag indicator**

### 📈 **Advanced Functionality**
- **JSON Storage**: Persistent data storage with automatic save/load
- **Timestamps**: Creation time tracking for each task
- **Categories**: Organize tasks by custom categories
- **Due Dates**: Track task deadlines
- **Priority Levels**: High/Medium/Low priority classification
- **Statistics Dashboard**: View task analytics and breakdowns

### 🎮 **Interactive Navigation**
- **Arrow Key Navigation**: Use ↑ ↓ arrows to navigate menu options
- **Visual Selection**: Clear highlighting of selected menu items
- **Responsive UI**: Real-time updates during navigation
- **Keyboard Shortcuts**: Quick navigation with Enter key

### 🎯 **Menu System**
- 📝 **Add New Task**: Create tasks with description, priority, category, and due date
- 👀 **View All Tasks**: Display comprehensive task table with all attributes
- ✏️ **Update Task**: Modify task details including priority, category, and due date
- 🗑️ **Delete Task**: Remove tasks with confirmation dialog
- ✅ **Toggle Complete**: Mark tasks as complete/incomplete
- 📊 **Statistics**: View task analytics and breakdowns
- 🚪 **Exit Application**: Gracefully close the application

## 🚀 Usage

1. Clone or download the repository
2. Run the application with Python:
   
3. Use the arrow keys (↑ ↓) to navigate through menu options
4. Press Enter to select the highlighted option
5. Follow the on-screen prompts for each operation

## 📋 Task Table Columns

The application displays tasks in a comprehensive table with the following columns:
- **ID**: Task identifier number
- **STATUS**: Completion status (✅ for completed, ⭕ for pending)
- **PRIO**: Priority level (🔴 High, 🟡 Medium, 🟢 Low)
- **DESCRIPTION**: Task description
- **CREATED AT**: Timestamp of task creation
- **DUE DATE**: Deadline for the task (if set)
- **CATEGORY**: Task category for organization

## ⚙️ Requirements

- Python 3.x
- No external dependencies required (uses built-in Python libraries only)

## 🛠️ Functionality

### Task Management
- **Add Tasks**: Create new tasks with descriptions, priority levels, categories, and due dates
- **View Tasks**: Display all tasks in a comprehensive table format
- **Update Tasks**: Modify task details including description, priority, category, and due date
- **Delete Tasks**: Remove tasks with confirmation dialog to prevent accidental deletion
- **Mark Complete**: Toggle task completion status with visual indicators
- **Statistics**: View comprehensive statistics including total tasks, completed/pending breakdown, and priority distribution

### Data Persistence
- All data is saved to  automatically
- Data persists between application sessions
- Robust error handling for file operations

### User Experience
- Clean, intuitive interface with clear visual hierarchy
- Responsive navigation with arrow key support
- Helpful error messages and prompts
- Confirmation dialogs for important actions
- Loading animations for better user experience

## 🎨 Color Scheme

The application uses a carefully designed color palette:
- **Headers**: Cyan and magenta for titles
- **Success**: Bright green for positive feedback
- **Warnings**: Bright yellow for caution messages
- **Errors**: Bright red for error messages
- **Task Status**: Green for completed, yellow for pending
- **Priority Indicators**: Red for high, yellow for medium, green for low

## 🏗️ Architecture

The application follows a clean, modular architecture:
- **Task Class**: Represents individual tasks with all attributes
- **TaskManager Class**: Handles data persistence and business logic
- **UIHelper Class**: Manages all UI formatting and display functions
- **InteractiveMenuHandler Class**: Handles menu navigation and user input processing

## 📊 Statistics Dashboard

The statistics feature provides valuable insights:
- Total tasks count
- Completed vs pending tasks breakdown
- Priority level distribution (High/Medium/Low)
- Visual representation of task data

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request to enhance the application further.

## 📄 License

This project is open source and available under the MIT License.

---

**Python Console Todo App** - A beautiful, functional, and modern console-based task management solution built with Python.
