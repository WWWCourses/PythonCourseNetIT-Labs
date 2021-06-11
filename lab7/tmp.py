import re


strings = ""
regex = re.compile(r"((?P<w>\w)(\d))\")

# [A-Za-z0-9_]
m = regex.search(string)
if m:
	print(m[0])
	# print(m[1])
else:
	print("No match")


