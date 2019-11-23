import pert


def test_layout_dimensions():
    project = pert.Project()
    project.addTask(pert.Task("My least favourite task"))
    box1 = pert.Box(pert.Task("task1"), width=10, height=20, x=12, y=100)

    assert (10 + 12, 100 + 20) == pert.find_layout_dimensions([box1])
