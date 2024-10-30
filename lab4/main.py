import parser.ready as ready
import parser.stupid as stupid
import parser.formal as formal
from parser.utils import node_to_string


# YAML to XML
if __name__ == '__main__':
    with open("schedule.yaml") as file:
        xml = stupid.parse(file)
        print(xml)

    with open("schedule.yaml") as file:
        xml = ready.parse(file)
        print(xml)

    with open("schedule.yaml") as file:
        tree = formal.parse(file)
        print(node_to_string(tree))

    # with open("schedule.xml", "w") as new_file:
    #   new_file.write(xml)

