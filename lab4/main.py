import parser.ready as ready
import parser.stupid as stupid
import parser.formal as formal
import parser.regular as regular


# YAML to XML
if __name__ == '__main__':
    with open("schedule.yaml") as file:
        xml = stupid.parse(file)
        print(xml)

    with open("schedule.yaml") as file:
        xml = ready.parse(file)
        #print(xml)

    with open("schedule.yaml") as file:
        xml = regular.parse(file)
        #print(xml)

    with open("schedule.yaml") as file:
        xml = formal.parse(file)
        #print(xml)

    # with open("schedule.xml", "w") as new_file:
    #   new_file.write(xml)

