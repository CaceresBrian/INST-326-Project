# task_list.py

from taskClass import Task

class TaskList:
    """
    Represents a named list of tasks.
    """

    def __init__(self, name):
        """
        Initialize a TaskList.

        :param name: Name of this task list (e.g., 'School', 'Work').
        """
        self.name = name
        self.tasks = []  # list of Task objects

    def __repr__(self):
        """
        Return a developer-friendly string representation of the TaskList.
        """
        return f"TaskList(name={self.name!r}, tasks={len(self.tasks)})"

    def add_task(self, task):
        """
        Add a Task to this list.

        :raises ValueError: if a task with the same title already exists.
        """
        for existing in self.tasks:
            if existing.title == task.title:
                raise ValueError("A task with this title already exists in this list.")
        self.tasks.append(task)

    def remove_task(self, title): # modified this
        """
        Remove a Task from this list by its title.

        :parameter title: The title of the task that is being removed
        :raises KeyError: if no task with that title exists.
        """
        task = self.get_task(title)
        if task:
            self.tasks.remove(task)
        else:
            raise KeyError(f"No task found with title: '{title}'.")

    def get_task(self, title):
        """
        Return the Task with the given title, or None if not found.
        
        :parameter title: The title of the task we are trying to find
        """
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def list_tasks(self, show_completed=None): #modified this
        """
        Return a list of tasks, optionally filtered by completion status

        :param show_completed:
            None -> return all tasks,
            True -> only completed tasks,
            False -> only incomplete tasks.
        
        :return: Shows the list of task objects that matches the filter (none, true, false)
        """
        if show_completed is None:
            return list(self.tasks) # <- this exits early if show_completed is none
        
        
        filtered = []
        for task in self.tasks:                
            if task.is_completed() == show_completed:
                filtered.append(task)
        return filtered

    def count_tasks(self):
        """
        Return the total number of tasks in this list.
        """
        return len(self.tasks)

    def count_completed(self): ### Modified this
        """
        Return the number of completed tasks in this list.
        """
        return len(self.list_tasks(show_completed=True))

    def count_pending(self): ### Modified this
        """
        Return the number of incomplete (pending) tasks in this list.
        """
        return len(self.list_tasks(show_completed=False))

    def find_tasks(self, keyword):
        """
        Return a list of tasks whose title or notes contain the given keyword.
        
        :parameter keyword: The specific string to look for in the task titles or notes
        """
        matches = []
        for task in self.tasks:
            if task.matches_query(keyword):
                matches.append(task)
        return matches
    
    def to_lines(self): # modified this
        """
        Convert this TaskList and its tasks to lines of text for saving to a file.

        Format:
        LIST|<list_name>
        TASK|title|due_date|priority|completed|notes
        
        The 'completed' field is determined using task.is_completed()
        to ensure consistency. It is stored as "1" if True, "0" if False
        """
        lines = []
        lines.append("LIST|{}\n".format(self.name))
        for task in self.tasks:
            
        # The 'completed' field is determined using task.is_completed()
            completed_flag = "1" if task.is_completed() else "0"
            
            # To keep it simple, we replace newlines in notes with spaces.
            # This will also handle None notes
            safe_notes = (task.notes or "").replace("\n", " ")
            
            # lets build the line
            line = "TASK|{}|{}|{}|{}|{}\n".format(
                task.title,
                task.due_date,
                task.priority,
                completed_flag,
                safe_notes
            )
            lines.append(line)
        return lines
