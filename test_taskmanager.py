from task_manager import TaskManager
from taskListClass import TaskList
from taskClass import Task


def test_add_and_get_list():
    manager = TaskManager()
    task_list = TaskList("School")

    manager.add_list(task_list)

    assert manager.get_list("School") is task_list
    assert len(manager.list_all_lists()) == 1

def test_find_tasks_global_searches_all_lists():
    manager = TaskManager()

    school = TaskList("School")
    personal = TaskList("Personal")

    school.add_task(Task("Finish Homework", notes="calculus"))
    personal.add_task(Task("Buy milk", notes="grocery"))

    manager.add_list(school)
    manager.add_list(personal)

    matches = manager.find_tasks_global("milk")

    assert len(matches) == 1
    assert matches[0].title == "Buy milk"

def test_save_and_load_file():
    manager = TaskManager()

    school = TaskList("School")
    school.add_task(
        Task(
            "Finish Homework",
            due_date="2025-12-01",
            priority="high",
            notes="calculus"
        )
    )
    manager.add_list(school)

    filename = "test_tasks.txt"
    manager.save_to_file(filename)

    new_manager = TaskManager()
    new_manager.load_from_file(filename)

    loaded_list = new_manager.get_list("School")
    assert loaded_list is not None

    tasks = loaded_list.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Finish Homework"
    assert tasks[0].due_date == "2025-12-01"
    assert tasks[0].priority == "high"
    assert tasks[0].notes == "calculus"
