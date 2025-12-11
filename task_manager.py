# This is the task_manager class 
# This will include methods to initialize task list objects

from task_list import TaskList
from task import Task

class TaskManager:
    """
    Houses all the methods dealing with task list objects
    """
    
    def __init__(self):
        """
        Used to initialize and empty task manager. 
        """
        self.lists = {}
        
        
    def __repr__(self):
        """
        Used to create a string representation for the task manager
        """
        return "taskManager(num_lists = {})".format(len(self.lists))
    
    def add_list(self, task_list):
        """
        Adds a task list to this manager
        """
        self.lists[task_list.name] = task_list

    def remove_list(self, name):
        """
        Removes the called list from the task list 
        """
        del self.list[name]
    
    def get_list(self, name):
        """
        Returns the task list that was called
        """
        return self.list.get(name)
    
    def list_all_lists(self):
        """
        Returns the names of all the list in the task list
        """
        return list(self.lists.values())
    
    def list_all_task(self):
        """
        Returns the names of all the task found in across all the list
        """
        all_tasks = []
        for task_list in self.lists.values():
            for task in task_list.tasks:
                all_tasks.append(task)
        return all_tasks
                
    def find_tasks_global(self, keyword):
        """
        Looks across all lists and returns task containing the keyword
        """
        matches = []
        for task_list in self.lists.values():
            matches.extend(task_list.find_tasks(keyword))
        return matches

    def save_to_file(self, filepath):
        """
        Save all the list and the tasks to a text file
        """
        f = open(filepath, "w")
        try:
            for task_list in self.lists.values():
                lines = task_list.to_lines()
                for line in lines:
                    f.write(line)
        finally:
            f.close()
            
    def load_from_file(self, filepath):
        pass        
        
        
        
    