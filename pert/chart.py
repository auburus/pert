import random
from enum import Enum

from . import formatters


class Box:
    def __init__(self, task, width, height, x=0, y=0):
        self._task = task
        self._width = width
        self._height = height
        self.x = x
        self.y = y

    @property
    def task(self):
        return self._task

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def arrow_origin(self):
        return (int(self.x + self._width), int(self.y + self._height / 2))

    @property
    def arrow_destination(self):
        return (int(self.x), int(self.y + self._height / 2))

class BoxBuilder:
    """
    This object exists to ensure that all different
    boxes are created with a common width and height
    """

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def build(self, task):
        return Box(task, self._width, self._height)


class Arrangement(Enum):
    Random = 1

    @staticmethod
    def get(arrangement):
        return {Arrangement.Random: RandomArrangement()}[arrangement]


class RandomArrangement:
    def rearrange(self, boxes):
        """
        Immutable method that rearranges the boxes
        """
        new_boxes = boxes.copy()

        for box in new_boxes:
            box.x = random.randint(0, 1000 - box.width)
            box.y = random.randint(0, 600 - box.height)

        return new_boxes


class Chart:
    def __init__(
        self, project, arrangement=Arrangement.Random, box_builder=BoxBuilder(150, 90)
    ):
        self._project = project
        self._boxes = Arrangement.get(arrangement).rearrange(
            [box_builder.build(task) for task in project.tasks]
        )
        self._arrangement = arrangement

    def find_box(self, task):
        return next(b for b in self._boxes if b.task == task)

    @property
    def boxes(self):
        return self._boxes

    def find_dependencies(self, box):
        return map(lambda t: self.find_box(t), self._project.findDependencies(box.task))

    def save(self, filepath, format):
        if format == "svg":
            output = formatters.svg(self)
        else:
            raise RuntimeError("Invalid format <{}>".format((format)))


        with open(filepath, "w") as f:
            f.write(output)
