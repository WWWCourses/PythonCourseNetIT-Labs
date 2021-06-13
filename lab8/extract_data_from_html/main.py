import re

def read_file_as_string(path):
	pass

def write_to_file(path,string):
	pass


def extract_and_store_data(html):
	rx = re.compile(r'')
	res = rx.findall(html)

	for r in res:
		print(f'{r[0]}-{r[1]}')
		write_to_file('data/ouput.txt',f'{r[0]}-{r[1]}\n')



html = read_file_as_string('html/test.html')
# print(html)

data = extract_and_store_data(html)

