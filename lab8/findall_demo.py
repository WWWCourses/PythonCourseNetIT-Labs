import re

string = '''
	line1
	# line 2
	line3
	# line 4
	line5
	line6
line 7
'''

rx = re.compile(r'(?m)^\s*([a-z]+)(\d+)')

res = rx.findall(string)
print(res)
