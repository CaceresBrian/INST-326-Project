# INST-326-Project
**Task Management Application**

## Group Members/Roles
- **Riley Coleman** – Team coordination, communication with project mentor, and testing  
- **Fabricio** – Software development and feature development  
- **Brian Caceres** – Software development and feature development  
- **Kevin Kim** – Testing and documentation  

### Individual Responsibilities
- **Member 1:** Task and task logic (add/edit/delete)  
- **Member 2:** TaskManager (task categorization, listing, searching)  
- **Member 3:** Reminder system (set due dates, check due dates, simulate notifications)  
- **Member 4:** User management and possible calendar view or persistence (saving/loading tasks)  

---

## Project Overview
The purpose of the application is to allow users to create, organize, and manage tasks using object-oriented programming concepts such as classes, objects, and methods.

Users can add tasks, assign them to categories, view task lists, and manage due dates through a simple command-line interface.

---

## File Descriptions
The repository is organized into multiple Python files, each responsible for a specific part of the application:

- **`main.py`**  
  The entry point of the program. This file runs the application and allows users to interact with the task management system.

- **`taskClass.py`**  
  Defines the `Task` class, which represents individual tasks.

- **`taskListClass.py`**  
  Defines the `TaskList` class, which stores and manages collections of tasks.

- **`task_manager.py`**  
  Handles higher-level task operations such as adding, categorizing, searching, and listing tasks.

- **`userClass.py`**  
  Defines the `User` class, which represents users and associates tasks with specific users.

- **`test_task.py`**  
  Unit tests for validating the behavior of the `Task` class.

- **`test_tasklist.py`**  
  Unit tests for validating the behavior of the `TaskList` class.

- **`test_taskmanager.py`**  
  Unit tests for validating the behavior of the `TaskManager`.

---

## How to Run the Program
  When the program runs, the user interacts with the application through the command line
  The user is prompted to:
  1. Create new tasks
  2. Assign tasks to categories
  3. View all tasks or tasks by category
  4. Edit or delete existing tasks
  5. Check task due dates and reminders

## Program Output Explained
  The program outputs text to the terminal that reflects the current state of the system which includes:
  1. Confirmation messages when tasks are successfully added, edited or deleted
  2. List of tasks displayed by category or user
  3. Task details such as title, category, and due date
  4. Messages indicating when tasks are due or overdue
This will make it easier for thge user to understand their task status and manage responibilites in the best possible manner

### Requirements
- Python 3.x installed on your machine

### Steps
1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the program using the command:

```bash
python main.py
   





