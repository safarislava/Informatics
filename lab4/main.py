import parser.ready as ready
import parser.stupid as stupid
import parser.formal as formal
import parser.regular as regular
import time


def create_xml(s, index=""):
    with open(f"schedule{index}.xml", "w") as new_file:
        new_file.write(s)


def test(func, s, n=1000):
    t1 = time.time()
    for i in range(n):
        func(s)
    t2 = time.time()
    delta = t2 - t1
    print(delta)
    return delta


# YAML to XML
if __name__ == '__main__':
    with open("schedule.yaml") as file:
        s = file.read()

    create_xml(regular.parse(s), "_regular")

    # test(stupid.parse, s)
    # test(formal.parse, s)
    # test(regular.parse, s)
    # test(ready.parse, s)
