import json, sys


def load_data(filepath):
	with open(filepath, 'r') as file_to_convert:
		file_content_json = json.loads(file_to_convert.read())
	return file_content_json

def pretty_print_json(text_json):
	print(json.dumps(text_json, sort_keys=True, indent=4, ensure_ascii=False))


def main():
	text_json = load_data(sys.argv[1])
	pretty_print_json(text_json)

if __name__ == '__main__':
    main()
