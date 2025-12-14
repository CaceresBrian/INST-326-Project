# This is the main file. This will display the menu which the user will interact with.
# This file will house the menu display and interaction methods

from task_manager import TaskManager
from taskListClass import TaskList
from taskClass import Task


def ask_list_name():
    """
    Will ask the user to input a name for the list they wish to create or interact with
    """
    list_name = input("Enter a list name: ").strip()
    
    return list_name

def ask_task_name():
    """
    Will ask the user to input a name for the task they are about to input
    """
    task_name = input("Enter the name of your task").strip()

    return task_name

def ask_priority_of_task():
    """
    Will ask the user to input the priority of the task (High, Medium, Low)
    """
    
    priority = input("What is the priority for this task? High, Medium, or Low (if left blank, the defualt will be medium)").strip().lower()
    if not priority:
        priority = "medium"
        
    return priority

def ask_due_date():
    """
    Will ask the user the due date
    """
        
    due_date = input("What is the due date? Example: 2025-9-04").strip()
    
    return due_date

def ask_notes():
    """
    Will ask the user to input notes for the task 
    """
    
    notes = input("What are the notes for this task?").strip()
    
    return notes
    
def main():
    """
    This is where the interactive menu will live and we will run all interactions through here. 
    The menu will appear at the end of every interaction 
    """
    
    manager = TaskManager()
    
    while True:
        print("\n***** TORTUGA TASK MANAGER MENU *****\n")
        print("\n  *** Please choose an option   ***\n")
        print("1) Create a new task list")
        print("2) View all  list")
        print("3) Add a task to an existing list")
        print("4) View the task(s) that in a list")
        print("5) Mark task as complete or incomplete")
        print("6) Search task by keyword")
        print("7) Save all to a text file")
        print("8) Load task from a text file")
        print("9) Quit Tortuga Task Manager")

        choice = input("Option: ").strip()
        
        if choice == "1":
            name = ask_list_name()
            task_list = TaskList(name)
            manager.add_list(task_list)
            
            
            
        elif choice == "2":
            list = manager.list_all_lists()
            if not list:
                print("There are no task list yet.\n")
            else:
                print("Task List:\n")
                for task_list in list:
                    print("*{} ({} task, {} completed)".format(task_list.list_tasks(), task_list.count_tasks(), task_list.count_completed()))
                    
        elif choice == "3":
            name = ask_list_name()
            task_list = manager.get_list(name)
            
            if task_list is None:
                print("There is not a task list with that name. Please try again \n")
                continue
            
            title = ask_task_name()
            due_date = ask_due_date()
            priority = ask_priority_of_task()
            notes = ask_notes()
            task = Task(title, due_date, priority, notes)
            
            task_list.add_task(task)
            print("\nTask successfuly added :)\n")
            


        elif choice == "4":
            name = ask_list_name()
            task_list = manager.get_list(name)
            
            if task_list is None:
                print("There is not a task list with that name. Please try again \n")
                continue
            
            tasks = task_list.list_task()
            
            if not tasks:
                print("There are no task in that list")
            else:
                print("Task in list '{}': ".format(task_list.list_tasks()))
                for task in tasks:
                    status = "Completed" if task.is_completed() else "Pending"
                    print("\n- {} [{}] (Due: {}, Priority: {})".format(task.title,
                                                                       status,
                                                                       task.due_date or "none",
                                                                       task.priority))
            

        elif choice == "5":
            name = ask_list_name()
            task_list = manager.get_list(name)
            
            if task_list is None:
                print("There is no list with that name, please try again.")
                continue
            
            name = ask_task_name
            task = task_list.get_task(name)
            
            if task is None:
                print("There is no task with that title in this list. Please try again")
                continue
            
            print("Current list status:", "completed" if task.is_completed() else "incomplete/pending")
            
            new_status = input("Is this task (c)ompleted or (i)ncomplete").strip().lower()
            
            if new_status == "c":
                task.mark_completed()
                print("Task is now marked as completed.")
            elif new_status == "i":
                task.mark_incomplete()
                print("Task is now marked incomplete/pending.")
            else:
                print("No changes made")


        elif choice == "6":
            keyword = input("Please enter a keyword: ").strip()
            matches = manager.find_tasks_global(keyword)
            
            if not matches:
                print("There are no task matching that keyword.")
            else:
                print("Matching tasks:")
                for task in matches:
                    print("- {}, (priority: {}, completed: {})".format(
                        task.title, 
                        task.priority, 
                        task.is_completed()
                    ))



        elif choice == "7":
            path = input("Enter the file path to save: ").strip()
            manager.save_to_file(path)
            print("Successfully saved to ", path)


        elif choice == "8":
            path = input("Enter the file path to load: ").strip()
            manager.load_from_file(path)
            
            print("File succesfully loaded.")
            

        elif choice == "9":
            break


if __name__ == "__main__":
    main()
