class Node:
    tag = ""
    value = ""

    def __init__(self, tag="", value=""):
        self.tag = tag
        self.value = value


def node_to_string(node):
    if not type(node.value) is list:
        return f"{node.tag} - {node.value}\n"
    else:
        s = node.tag + ":\n"
        for i in node.value:
            s += add_tab(node_to_string(i))
        return s


def count_front_spaces(s):
    count = 0
    for c in s:
        if c != ' ':
            return count
        count += 1
    return 0


def remove_front_spaces(s):
    for i in range(len(s)):
        if s[i] != ' ':
            return s[i:]


def add_tab(s):
    res = ""
    for line in s.split("\n")[:-1]:
        res += " " * 4 + line + "\n"
    return res