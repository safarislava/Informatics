from parser.utils import *


def parse(file):
    xml = parse_string(file.read())
    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + xml
    return xml


def parse_string(s, parent_tag=""):
    spacing = count_front_spaces(s)

    parents = []
    parent = s.split("\n", 1)[0] + "\n"
    for line in s.split("\n")[1:-1]:
        if count_front_spaces(line) == spacing:
            parents.append(parent)
            parent = line + "\n"
        else:
            parent += line + "\n"
    parents.append(parent)

    xml = ""
    for parent in parents:
        tag = remove_front_spaces(parent.split(":", 1)[0])

        if tag[0] == "-":
            xml += f"<{parent_tag}>\n"
            xml += add_tab(parse_string(parent.replace("-", " ", 1)))
            xml += f"</{parent_tag}>\n"
            continue

        value = parent.split(":", 1)[1]

        if value.count("\n") == 1:
            value = value.split("\n", 1)[0][1:]
            xml += f"<{tag}>{value}</{tag}>\n"
            continue

        children = parent.split("\n", 1)[1]

        if remove_front_spaces(children)[0] == "-":
            xml += parse_string(children, tag)
            continue

        xml += f"<{tag}>\n"
        xml += add_tab(parse_string(children))
        xml += f"</{tag}>\n"

    return xml
