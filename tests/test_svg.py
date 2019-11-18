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
    project.addTask(pert.Task("My least favourite task"))
    project.addTask(pert.Task("Create a new test for the current suite"))
    project.addTask(
        pert.Task("Transform fossil from lab into a live and dangerous dinosaur")
    )

    svg = pert.SVG.fromProject(project)
    svg.arrange(pert.Arrangement.Random)
    svg.save(output_file)

    assert os.path.isfile(output_file)

    with open(output_file) as f:
        assert svg.svg == f.read()
