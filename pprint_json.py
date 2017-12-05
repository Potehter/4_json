import json, sys


def load_data(filepath):
    f = open(filepath, 'r')
    file_json = json.loads(f.read())
    return file_json

def pretty_print_json(data):
	print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))

def get_filepath():
	return sys.argv[1]

def main():
	filepath = get_filepath()
	data = load_data(filepath)
	pretty_print_json(data)

if __name__ == '__main__':
    main()
