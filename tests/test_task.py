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
