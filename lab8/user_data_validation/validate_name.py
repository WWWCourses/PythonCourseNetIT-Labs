import re


''' Description:
	User name must follow next rules:
	1. Must consists of 3 to 10 characters inclusive
	2. Username can only contain alphanumeric characters, dashes (-) and underscores (_).
	3. The first character of the username must be an alphabetic character

	Tip:
		We may use positive lookahead (https://www.regular-expressions.info/lookaround.html), to test for second condition
'''

def validate_name(string):
	rx = re.compile(r'''(?x)
	^[a-zA-Z]  		# rule 3
	 [\w-]{2,9}		# rule 1 and 2
	$
	''')

	m = rx.search(string)
	if m:
		print(f'{string} is valid!')
	else:
		print(f'{string} is NOT valid!')




tests = [
	"ada", 	# yes
	"a__", 	# yes
	"a12345", # yes
	"a1234567890", # no (rule 1)
	"1aaaaaaa", # no (rule 3)
	"-a-", 	# no (rule 3)
	"a", 	# no

]

for t in tests:
	validate_name(t)