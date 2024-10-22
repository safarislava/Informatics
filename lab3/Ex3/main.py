import re


def f(s):
    match = re.search(r'<meta.+name="daily_price".+(Bitcoin|BTC).+?(\d[\d,.]+).+RUB.*>', s)
    try:
        return match.group(2)
    except AttributeError:
        return ""


for i in range(1, 7):
    with open(f"test/{i}", 'r') as file:
        s = file.read()

    with open(f"test/{i}.a", 'r') as file:
        ans = file.readline()

    if ans == f(s):
        print(f"Test {i} is right")
    else:
        print(f"Test {i} is failed")
