import pytest
from taskClass import Task
from taskListClass import TaskList

def test_add_task_increases_count():
    task_list = TaskList("School")
    task = Task("Finish Homework")

    task_list.add_task(task)

    assert task_list.count_tasks() == 1
    assert task_list.get_task("Finish Homework") is task

def test_add_duplicate_task_raises_error():
    task_list = TaskList("School")
    task1 = Task("Finish Homework")
    task2 = Task("Finish Homework")

    task_list.add_task(task1)

    with pytest.raises(ValueError):
        task_list.add_task(task2)
        
def test_remove_task_removes_it():
    task_list = TaskList("School")
    task = Task("Finish Homework")
    task_list.add_task(task)

    task_list.remove_task("Finish Homework")

    assert task_list.count_tasks() == 0
    assert task_list.get_task("Finish Homework") is None


def test_remove_missing_task_raises_error():
    task_list = TaskList("School")

    with pytest.raises(KeyError):
        task_list.remove_task("Does Not Exist")

