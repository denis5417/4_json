import json
import sys
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        print("Неверный путь к файлу")
        return None
    with open(filepath) as file_handler:
        try:
            return json.load(file_handler)
        except json.decoder.JSONDecodeError:
            print("В файле не JSON")
            return None


def pretty_print_json(parsed_json):
    if not parsed_json:
        pass
    else:
        print(json.dumps(parsed_json, indent=4, sort_keys=True))


if __name__ == '__main__':
    try:
        pretty_print_json(load_data(sys.argv[1]))
    except IndexError:
        print("Укажите путь к файлу")
