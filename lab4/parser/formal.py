from parser.utils import *


def parse(s):
    tree = parse_tree(s)[0]
    xml = tree_to_xml(tree)
    return xml


def parse_tree(s, parent_tag=""):
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
            node.value = parse_tree(parent.replace("-", " ", 1))
            res.append(node)
            continue

        value = parent.split(":", 1)[1]

        if value.count("\n") == 1:
            node = Node(tag, value.split("\n", 1)[0][1:])
            res.append(node)
            continue

        children = parent.split("\n", 1)[1]

        if remove_front_spaces(children)[0] == "-":
            for i in parse_tree(children, tag):
                res.append(i)
            continue

        node = Node(tag)
        node.value = parse_tree(children)
        res.append(node)

    return res


def tree_to_xml(node):
    if not type(node.value) is list:
        return f"<{node.tag}>{node.value}</{node.tag}>\n"
    else:
        s = f"<{node.tag}>\n"
        for i in node.value:
            s += add_tab(tree_to_xml(i))
        s += f"</{node.tag}>\n"
        return s