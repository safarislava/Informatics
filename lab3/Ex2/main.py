import re


def f(s):
    words = " ".join(re.findall(r"\w+", s))  # without special characters

    matches = []
    match = re.search(r"\bВТ\s(\w+\s){0,4}ИТМО\b", words)
    while match:
        matches.append(match.group(0))
        words = words[match.start() + 2:]
        match = re.search(r"\bВТ\s(\w+\s){0,4}ИТМО\b", words)

    return matches


for i in range(1, 6):
    with open(f"test/{i}", 'r') as file:
        s = file.read()

    with open(f"test/{i}.a", 'r') as file:
        ans = list(map(lambda x: x.replace("\n", ""), file.readlines()))

    if ans == f(s):
        print(f"Test {i} is right")
    else:
        print(f"Test {i} is failed")
