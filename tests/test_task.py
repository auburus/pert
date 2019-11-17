import pytest
import pert


def test_defaultcreation():
    task = pert.Task(
        id="BRAVO-254",
        title="task title",
        description="Very important task that does a very important thing",
    )

    assert task.id == "BRAVO-254"
    assert task.title == "task title"
    assert task.description == "Very important task that does a very important thing"


def test_default_title():
    task = pert.Task(id="BRAVO-254")

    assert task.title == "BRAVO-254"


# def test_depends():
#     task1 = pert.Task(id="123")
#     task2 = pert.Task(id="245")
#
#     task3 = pert.Task(id="21",
#                       dependencies=[task1, task2])
#
#     assert task3.dependencies == [task1, task2]
#
# def test_invalid_depends():
#     task1 = pert.Task(id="123")
#
#     with pytest.raises(AttributeError) as exception:
#         task2 = pert.Task(id="456",
#                           dependencies=["123"])
#
