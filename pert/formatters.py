def find_layout_dimensions(boxes):
    """
    Find the dimensions of the smallest rectangle that fits
    all the boxes, starting from (0,0)
    """
    box_max_x = max(boxes, key=lambda box: box.x)
    max_x = box_max_x.x + box_max_x.width

    box_max_y = max(boxes, key=lambda box: box.y)
    max_y = box_max_y.y + box_max_y.height

    return (max_x, max_y)


def svg(boxes):
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

    def svg_from_box(box):
        rect = (
            '<rect height="{}" width="{}" x="{}" y="{}" rx="15" '
            'stroke-width="3" stroke="#000000" fill="#66a266" />\n'.format(
                box.height, box.width, box.x, box.y
            )
        )

        # TODO Remove magic numbers
        title = (
            '<text x="{x}" y="{y}" font-size="14">\n'
            + wrapText(box.task.title, 17)
            + "</text>\n"
        )
        title = title.format(x=box.x + 10, y=box.y + 10)

        return "<g>\n" + rect + title + "</g>\n"

    width, height = find_layout_dimensions(boxes)
    width, height = width + 6, height + 6  # Account for the width of the border (3+3)

    return (
        '<?xml version="1.0" standalone="no"?>\n'
        '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
        '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'
        '<svg width="{width}" height="{height}" version="1.1" xmlns="http://www.w3.org/2000/svg">\n'
        "<desc>PERT Chart</desc>\n"
        + '<rect width="100%" height="100%" fill="#ffffff"/>\n'
        + "\n".join(map(svg_from_box, boxes))
        + "</svg>"
    ).format(width=width, height=height)
