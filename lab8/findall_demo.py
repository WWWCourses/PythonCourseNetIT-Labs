import re

file_content = '''
	line1
		# line2
	line3
# line 4
	line5
	line6
line7
'''

beautified_file_content = ""

# we need 'm' (multiline) flag because we want '^' and '$'
# to match beginning and end of each line
rx = re.compile(r'(?m)^\s*([a-z]+)(\d+)')

res = rx.findall(file_content)

for r in res:
	# print(f'{r[0]}-{r[1]}')
	beautified_file_content += f'{r[0]}-{r[1]}\n'

print(beautified_file_content)
