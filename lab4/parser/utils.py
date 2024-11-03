class Node:
    tag = ""
    value = ""

    def __init__(self, tag="", value=""):
        self.tag = tag
        self.value = value


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