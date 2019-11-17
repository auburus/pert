from enum import Enum


class Task:
    """ Task data object
	This object just holds the information that makes a task a task,
	but it doesn't track any of the task's dependencies
	"""

    def __init__(self, id, title=None, description=""):
        self._id = id
        self._title = title if title else id
        self._description = description

    def __repr__(self):
        return "<{}>".format(self.id)

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description


class DependencyType(Enum):
    DEPENDS_ON = 1


class Dependency:
    """
	Tracks the dependency between two individual tasks
	"""

    def __init__(self, task1, task2, type):
        self.task1 = task1
        self.task2 = task2
        self.type = type


class Project:
    """
	Effectively, this is a Directed Acyclic Graph (DAG)
	with some extra handy functions
	"""

    def __init__(self):
        self._tasks = []
        self._dependencies = []

    def findTask(self, id):
        node = self._findTask(id)
        if node is None:
            raise AttributeError("Unable to find task with id {}".format(id))

        return node

    def _findTask(self, id):
        return next((task for task in self._tasks if task.id == id), None)

    def addTask(self, task, depends_on=[]):
        if self._findTask(task.id) is not None:
            raise AttributeError(
                "Task <{}> already exists in this project.".format(task)
            )

        dependencies = []
        for t in depends_on:
            if t not in self._tasks:
                raise AttributeError(
                    "Task <{task1}> depends on task <{task2}>, but <{task2}> is"
                    "not in project".format(task1=task, task2=t)
                )

            dependencies.append(Dependency(task, t, DependencyType.DEPENDS_ON))

        self._tasks.append(task)
        self._dependencies.extend(dependencies)

    def findDependencies(self, task):
        return [
            d.task2
            for d in self._dependencies
            if d.task1 == task and d.type == DependencyType.DEPENDS_ON
        ]
