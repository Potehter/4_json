import json, sys


def load_data(filepath):
    file_origin = open(filepath, 'r')
    file_json = json.loads(f.read())
    return file_json

def pretty_print_json(text_json):
	print(json.dumps(text_json, sort_keys=True, indent=4, ensure_ascii=False))

def get_filepath():
	return sys.argv[1]

def main():
	filepath = get_filepath()
	text_json = load_data(filepath)
	pretty_print_json(text_json)

if __name__ == '__main__':
    main()
