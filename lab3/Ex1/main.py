import re


def f(s):
    return len(re.findall(r"X-\{P", s))


for i in range(1, 6):
    with open(f"test/{i}", 'r') as file:
        s = file.read()

    with open(f"test/{i}.a", 'r') as file:
        ans = int(file.read())

    if ans == f(s):
        print(f"Test {i} is right")
    else:
        print(f"Test {i} is failed")
