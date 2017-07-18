import json
import sys

def load_data(filepath):
    with open(filepath) as handle:
        parsed_json = json.load(handle)
    return parsed_json

def pretty_print_json(parsed_json):
    print(json.dumps(parsed_json, indent=4, sort_keys=True))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
