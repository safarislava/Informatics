from parser.utils import remove_front_spaces, count_front_spaces


def parse(s):
    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"

    spacing_list = []
    tag_list = []

    for line in s.split("\n")[:-1]:
        spacing = count_front_spaces(line.split(":", 1)[0])

        if len(spacing_list) > 0:
            while spacing_list[-1] >= spacing:
                xml += " " * spacing_list[-1] + f"</{tag_list[-1]}>\n"
                spacing_list.pop()
                tag_list.pop()

        tag = remove_front_spaces(line.split(":", 1)[0])
        if tag[0] == "-":
            tag = tag[2:]
            spacing += 2

            if xml.split("\n")[-2] != " " * spacing_list[-1] + f"<{tag_list[-1]}>":
                xml += " " * spacing_list[-1] + f"</{tag_list[-1]}>\n"
                xml += " " * spacing_list[-1] + f"<{tag_list[-1]}>\n"

        if ":" in line:
            value = line.split(":", 1)[1][1:]
        else:
            value = ""

        spacing_list.append(spacing)
        tag_list.append(tag)

        xml += spacing * " " + f"<{tag}>\n"
        if value != "":
            xml += spacing * "  " + f"{value}\n"

    while spacing_list:
        xml += " " * spacing_list[-1] + f"</{tag_list[-1]}>\n"
        spacing_list.pop()
        tag_list.pop()

    return xml
