class SVGChart:
    def __init__(self, project):
        self._project = project

    def save(self, filepath):
        with open(filepath, "w") as f:
            f.write(self.getContents())

    def getContents(self):
        return (
            '<?xml version="1.0" standalone="no"?>'
            '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"'
            '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
            '<svg version="1.1" xmlns="http://www.w3.org/2000/svg">'
            "<desc>PERT Chart</desc>" + self._getElementsAsSVG() + "</svg>"
        )

    def _getElementsAsSVG(self):
        return ""
