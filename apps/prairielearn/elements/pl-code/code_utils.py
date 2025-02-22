def parse_highlight_lines(highlight_lines: str) -> list[int] | None:
    """
    Parses a string like "1", "1-4", "1-3,5,7-8" into a list of lines like
    [1], [1,2,3,4], and [1,2,3,5,7,8]
    """
    lines = []
    components = highlight_lines.split(",")
    for raw_component in components:
        component = raw_component.replace(" ", "").split("-")
        try:
            if len(component) == 1:
                line = int(component[0])
                lines.append(line)
            # Try parsing as "##-###"
            elif len(component) == 2:
                start = int(component[0])
                end = int(component[1])
                lines.extend(range(start, end + 1))
            else:
                return None
        except ValueError:
            return None

    return lines
