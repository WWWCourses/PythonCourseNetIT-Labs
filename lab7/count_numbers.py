import re

string = "12 alakl 23klkl 45 jdkfj 89999, 1"
rx = re.compile(r"\d+")

results = rx.findall(string)
if results:
	print(len(results))