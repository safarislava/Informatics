from parser.utils import *


def parse(file):
    xml = parse_string(file.read())
    return xml[0]


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

    res = []
    for parent in parents:
        tag = remove_front_spaces(parent.split(":", 1)[0])

        if tag[0] == "-":
            node = Node(parent_tag)
            node.value = parse_string(parent.replace("-", " ", 1))
            res.append(node)
            continue

        value = parent.split(":", 1)[1]

        if value.count("\n") == 1:
            node = Node(tag, value.split("\n", 1)[0][1:])
            res.append(node)
            continue

        children = parent.split("\n", 1)[1]

        if remove_front_spaces(children)[0] == "-":
            for i in parse_string(children, tag):
                res.append(i)
            continue

        node = Node(tag)
        node.value = parse_string(children)
        res.append(node)

    return res
