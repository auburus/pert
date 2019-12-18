import pytest

import pert
import os


@pytest.fixture(scope="module")
def output_file():
    """
    Make sure that the file doesn't exist before the test
    """

    output_file = os.path.dirname(__file__) + "/output_file.svg"
    if os.path.isfile(output_file):
        os.remove(output_file)

    yield output_file


def test_save(output_file):
    project = pert.Project()
    task1 = pert.Task("My least favourite task")
    task2 = pert.Task("Create a new test for the current suite")
    task3 = pert.Task("Transform fossil from lab into a live and dangerous dinosaur")

    project.addTask(task1)
    project.addTask(task2, depends_on=[task1])
    project.addTask(task3, depends_on=[task1, task2])

    pert_chart = pert.Chart(project, arrangement=pert.Arrangement.Random)
    pert_chart.save(output_file, format="svg")

    assert os.path.isfile(output_file)

    # We could also check the contents of the file? It can't be
    # a random arrangement though, they need to be predictable
    # Maybe a validation file?
