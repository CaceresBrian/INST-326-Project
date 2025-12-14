import pytest
from taskClass import Task 

def test_task_creation():
    task = Task("Test Task")
    assert task.title == "Test Task"
    assert task.priority == "medium"
    assert task.is_completed() is False 

def test_task_empty_title_raises_error():
    with pytest.raises(ValueError):
        Task("")

def test_task_matches_query():
    task = Task("Finish Homework", notes="Work on calculus problems")
    assert task.matches_query("homework") is True
    assert task.matches_query("calculus") is True
    assert task.matches_query("history") is False



