import pert
import pytest


def test_findTask():
    project = pert.Project()

    with pytest.raises(AttributeError) as exception:
        project.findTask("asdf")

    # Check that the relevant key appears in the exception message
    assert "asdf" in str(exception.value)


def test_addTask():
    project = pert.Project()

    project.addTask(pert.Task("task1"))
    project.addTask(pert.Task("task2"))
    project.addTask(pert.Task("task3"))

    assert project.findTask("task1")
    assert project.findTask("task2")
    assert project.findTask("task3")


def test_dependencies():
    project = pert.Project()

    task1 = pert.Task("task1")
    task2 = pert.Task("task2")
    task3 = pert.Task("task3")

    project.addTask(task1)
    project.addTask(task2)
    project.addTask(task3, depends_on=[task1, task2])

    assert project.findDependencies(task1) == []
    assert project.findDependencies(task2) == []
    assert project.findDependencies(task3) == [task1, task2]
