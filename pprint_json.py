import json
import sys


def load_data(filepath):
    try:
        with open(filepath) as file_handler:
            return json.load(file_handler)
    except json.decoder.JSONDecodeError:
        print("В файле не JSON")
    except FileNotFoundError:
        print("Файл не найден")


def pretty_print_json(parsed_json):
    if not parsed_json:
        return None
    else:
        print(json.dumps(parsed_json, indent=4, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        pretty_print_json(load_data(sys.argv[1]))
    else:
        print("Укажите путь к файлу")
