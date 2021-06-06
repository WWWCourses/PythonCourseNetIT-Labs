import re

# Задача:
# За нас, валиден емайл адрес е всеки низ, който отговаря на следното условие:
	prefix@domain.tld
където
	prefix е:
		- поне 3 символа (които и да с)
	domain:
		-
 "<at least 3 symbols>@<at least 1 letter>.<at least 3 letters>"
user_mail = "alabala@test.com"


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
