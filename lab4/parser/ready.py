import yaml
from yaml import SafeLoader
import xmltodict


def parse(file):
    python_dict = yaml.load(file, Loader=SafeLoader)
    xml_string = xmltodict.unparse(python_dict, pretty=True, short_empty_elements=True)
    return xml_string
