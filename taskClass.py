class Task:
    """
    Represents a single task in the task manager.
    """

    def __init__(self, title, due_date="", priority="medium", notes="", completed=False): #modified this
        """
        Set up a Task.

        Arguments:
        title: The descriptive name of the task.
        due_date: The date this task is scheduled to be completed.
        priority: The importance level (must be one of the predefined strings).
        notes: Any additional comments.
        completed: A simple True/False status marker.

        """
        
        if not title:
            raise ValueError("Task title can not be empty.")
        if priority not in ("low", "medium", "high"):
            raise ValueError("Priority must be low, Medium, or high")
        
        self.title = title
        self.due_date = due_date
        self.priority = priority.lower()
        self.notes = notes or ""
        self.completed = completed

    def __repr__(self): # modified this
        """
        Return a developer-friendly string representation of the Task.
        """
        return (f"Task(title={self.title!r}, due_date={self.due_date!r}, "
            f"priority={self.priority!r}, notes={self.notes!r}, "
            f"completed={self.completed!r})")

    def mark_completed(self):
        """
        Mark this task as completed.
        """
        self.completed = True

    def mark_incomplete(self):
        """
        Mark this task as not completed.
        """
        self.completed = False

    def is_completed(self):
        """
        Return True if this task is completed, otherwise False.
        """
        return self.completed

    def update_title(self, new_title):
        """
        Update the title of this task.
        """
        self.title = new_title

    def update_due_date(self, new_due_date):
        """
        Update the due date of this task.
        """
        self.due_date = new_due_date

    def update_priority(self, new_priority): # modified this
        """
        Update the priority of this task.

        :raises ValueError: if priority is not 'low', 'medium', or 'high'.
        """
        allowed = ["low", "medium", "high"]
        if new_priority not in allowed:
            raise ValueError("Priority must be 'low', 'medium', or 'high'.")
        self.priority = new_priority

    def update_notes(self, new_notes):
        """
        Update the notes for this task.
        """
        self.notes = new_notes

    def matches_query(self, keyword): # modified this. 
        """
        Return True if the keyword appears in the title or notes (case-insensitive).
        """
        k = keyword.lower()
        
        if k in self.title.lower():
            return True
        
        if self.notes and k in self.notes.lower():
            return True
        
        return False
