import random
from enum import Enum

__all__ = ["SVG", "Dimensions", "Arrangement"]

WIDTH = 1024
HEIGHT = 640


class Arrangement(Enum):
    Random = 1

    @staticmethod
    def get(arrangement):
        return {Arrangement.Random: RandomArrangement()}[arrangement]


class RandomArrangement:
    def rearrange(self, boxes):
        for box in boxes:
            box.x = random.randint(0, WIDTH - box.dimensions.width)
            box.y = random.randint(0, HEIGHT - box.dimensions.height)


class Dimensions:
    def __init__(self, width, height, x_margin=0, y_margin=0):
        self.width = width
        self.height = height
        self.x_margin = x_margin
        self.y_margin = y_margin


class Box:
    def __init__(self, task, dimensions):
        self._task = task
        self.dimensions = dimensions
        self.x = 0
        self.y = 0

    @property
    def svg(self):
        rect = (
            '<rect height="{}" width="{}" x="{}" y="{}" rx="15" '
            'stroke-width="3" stroke="#000000" fill="#66a266" />\n'.format(
                self.dimensions.height, self.dimensions.width, self.x, self.y
            )
        )

        # TODO Remove magic numbers
        title = (
            '<text x="{x}" y="{y}" font-size="14">\n'
            + wrapText(self._task.title, 17)
            + "</text>\n"
        )
        title = title.format(x=self.x + 10, y=self.y + 10)

        return "<g>\n" + rect + title + "</g>\n"


def wrapText(text, maxLength):
    """ It assumes a maxLength>6
    """

    def in_tspan(text):
        return '<tspan x="{x}" dy="1em">' + text + "</tspan>\n"

    if len(text) < maxLength:
        return in_tspan(text)

    for i in range(maxLength, 1, -1):
        if text[i] == " ":
            return in_tspan(text[:i]) + wrapText(text[i + 1 :], maxLength)

    return in_tspan(text[: (maxLength - 1)] + "-") + wrapText(
        text[(maxLength - 1) :], maxLength
    )


class SVG:
    def __init__(self, boxes):
        self._boxes = boxes

    @staticmethod
    def fromProject(project, boxDimensions=Dimensions(150, 90, 10, 10)):
        boxes = []
        for task in project.tasks:
            boxes.append(Box(task, boxDimensions))

        return SVG(boxes)

    def save(self, filepath):
        with open(filepath, "w") as f:
            f.write(self.svg)

    def arrange(self, arrangement):
        strategy = Arrangement.get(arrangement)

        strategy.rearrange(self._boxes)

    @property
    def svg(self):
        return (
            '<?xml version="1.0" standalone="no"?>\n'
            '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
            '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'
            '<svg width="{width}" height="{height}" version="1.1" xmlns="http://www.w3.org/2000/svg">\n'
            "<desc>PERT Chart</desc>\n"
            + '<rect width="100%" height="100%" fill="#ffffff"/>\n'
            + "\n".join(map(lambda box: box.svg, self._boxes))
            + "</svg>"
        ).format(width=WIDTH, height=HEIGHT)
