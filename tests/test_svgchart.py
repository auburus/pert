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

    if os.path.isfile(output_file):
        os.remove(output_file)


def test_save(output_file):
    project = pert.Project()

    svg = pert.SVGChart(project)

    svg.save(output_file)

    assert os.path.isfile(output_file)

    with open(output_file) as f:
        assert svg.getContents() == f.read()
