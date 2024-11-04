from parser.utils import remove_front_spaces, count_front_spaces
import re

def parse(s):
    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"

    spacing_list = []
    tag_list = []
    pattern = re.compile(r"^(\s*)(.+?):(.*)$", flags=re.MULTILINE)
    f = re.findall(pattern, s)

    for i in range(len(f)):
        spacing = len(f[i][0])
        tag = f[i][1]
        value = f[i][2][1:]

        if len(spacing_list) > 0:
            while spacing_list[-1] >= spacing:
                xml += " " * spacing_list[-1] + f"</{tag_list[-1]}>\n"
                spacing_list.pop()
                tag_list.pop()

        if tag[0] == "-":
            tag = tag[2:]
            spacing += 2

            if xml.split("\n")[-2] != " " * spacing_list[-1] + f"<{tag_list[-1]}>":
                xml += " " * spacing_list[-1] + f"</{tag_list[-1]}>\n"
                xml += " " * spacing_list[-1] + f"<{tag_list[-1]}>\n"

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
