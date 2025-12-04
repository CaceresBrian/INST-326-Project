from datetime import date
from typing import Optional

class Task:
    """
    This will represent a task in our task management system
    It will store the title of the task, a description, a due date, and if it is completed or pending
    
    We are importing date from datetime because we want to store the due dates in a convenient format.
    We are also importing Optional from typing because due date will not always be required for user convenience 
    
    """
    
def __init__(self, title, description, priority, task_id, due_date: Optional[date] = None, completed:bool = False ):
    """
    Creates a new task
    
    """
    self.title = title
    self.description = description
    self.priority = priority
    self.task_id - task_id
    self.due_date = due_date
    self.completed = completed
    
    
    
def mark_completed(self):
    """
    will mark the task completed
    """
    self.completed = True
    
def mark_incomplete(self):
    """
    will mark the task as incomplete
    """
    self.completed = False
    
def is_overdue(self, today: Optional[date] = None) -> bool:
    """
    Takes todays date as an input and compares it the task due date. 
    Returns true if the task date exist, the task is incomplete, and today's date is after the task date
    
    """
    if self.due_date is None:
        return False
    
    return (not self.completed) and (today > self.due_date)

def set_due_date(self, new_date: Optional[date]):
    """
    Takes in a date as an input and modifies the due date for the selected task
    """
    self.due_date = new_date
    
def update_title(self, new_title):
    """
    Takes a string title as an input and modifies the title of the selected task 
    """    
    self.title = new_title
    
def update_description(self, new_desc):
    """
    takes in a string input and modifies the description of the selected task
    """    
    self.description = new_desc
    


    

    
    
    

    
    