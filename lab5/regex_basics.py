import re

# TASK: validate user email
# "<at least 3 symbols>@<at least 1 letter>.<at least 3 letters>"
user_mail = "alabala@test.com"

# pattern = r"a?a";
# strings = [
# 	"aa", # yes
# 	"a",  # yes
# 	"aaa",  # yes
# ]


# tel = r"\+359 [0-9]{8}"
pattern = r"[A-Z]{6}"
strings = [
	"IVANOV", 	#
	"Ivanov" # no
]

for str in strings:
	res = re.search(pattern, str)
	if res:
		print(f"{str} => {res}")
	else:
		print("no Match")
