import random

__all__ = ["SVG"]


class SVG:
    def __init__(self, project):
        self._project = project
        self._roundedBox = RoundedBox(150, 90)
        self.width = 1024
        self.height = 640

    def save(self, filepath):
        with open(filepath, "w") as f:
            f.write(self.getContents())

    def getContents(self):
        return (
            '<?xml version="1.0" standalone="no"?>\n'
            '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
            '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'
            '<svg width="{width}" height="{height}" version="1.1" xmlns="http://www.w3.org/2000/svg">\n'
            "<desc>PERT Chart</desc>\n"
            + '<rect width="100%" height="100%" fill="#ffffff"/>\n'
            + self._getElementsAsSVG()
            + "</svg>"
        ).format(width=self.width, height=self.height)

    def _getElementsAsSVG(self):
        elements = []
        for task in self._project.tasks:
            elements.append(
                self._roundedBox.create(
                    task,
                    random.randint(0, self.width - 150),
                    random.randint(0, self.height - 90),
                )
            )

        return "\n".join(elements)


class RoundedBox:
    def __init__(self, width, height, x_margin=30, y_margin=30):
        self.width = width
        self.height = height
        self.x_margin = x_margin
        self.y_margin = y_margin

    def create(self, task, x, y):

        box = (
            '<rect height="{}" width="{}" x="{}" y="{}" rx="15" '
            'stroke-width="3" stroke="#000000" fill="#66a266" />\n'.format(
                self.height, self.width, x, y
            )
        )
        title = (
            '<text x="{x}" y="{y}" font-size="14">\n'
            + wrapText(task.title, 17)
            + "</text>"
        )
        title = title.format(x=x + 10, y=y + 10)

        return "<g>\n" + box + title + "</g>\n"


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
