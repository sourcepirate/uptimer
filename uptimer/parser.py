from os import getcwd
from os.path import join, abspath
import yaml

def parse_domain(filename: str):
    filepath = abspath(join(getcwd(), filename))
    return yaml.safe_load(open(filepath, "r"))["domains"]
