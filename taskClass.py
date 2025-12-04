from datetime import date
from typing import Optional

class Task:
    """
    This will represent a task in our task management system
    It will store the title of the task, a description, a due date, and if it is completed or pending
    
    We are importing date from datetime because we want to store the due dates in a convenient format.
    We are also importing Optional from typing because due date will not always be required for user convenience 
    
    """
    
def __init__(self, title, description, due_date: Optional[date] = None, completed:bool =False)
    """
    Creates a new task
    
    """
    self.title = title
    self.description = description
    self.due_date = due_date
    self.completed = completed
    
def mark_completed():
    """
    will mark the task completed
    """
    self.completed = True
    
def mark_pending():
    """
    will mark the task as incomplete
    """
    self.comppleted = False
    
    

    
    