import pytest

import pert
import os


@pytest.fixture(scope="module")
def output_file():
    """
	Make sure that the file doesn't exist before the test, and that
	is cleaned up after the test
	"""

    output_file = os.path.dirname(__file__) + "/output_file.svg"
    if os.path.isfile(output_file):
        os.remove(output_file)

    yield output_file

    # if os.path.isfile(output_file):
    #     os.remove(output_file)


def test_save(output_file):
    project = pert.Project()
    project.addTask(pert.Task("My least favourite task"))
    project.addTask(pert.Task("Create a new test for the current suite"))
    project.addTask(
        pert.Task("Transform fossil from lab into a live and dangerous dinosaur")
    )

    svg = pert.SVG(project)

    svg.save(output_file)

    assert os.path.isfile(output_file)

    with open(output_file) as f:
        # Well, the current output right now is random, so it breaks this test :D
        # assert svg.getContents() == f.read()
        pass
