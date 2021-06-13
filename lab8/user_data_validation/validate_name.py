import re


''' Description:
	User name must follow next rules:
	1. Must consists of 3 to 10 characters inclusive.
	2. Username can only contain alphanumeric characters, dashes (-) and underscores (_).
	3. The first character of the username must be an alphabetic character
'''

def validate_name(string):
	# "x" flag ignores spaces and comments in a regex
	rx = re.compile(r'''(?x)
	^					# beginning of string
		[a-zA-Z]  		# rule 3
	 	[\w-]{2,9}		# rule 1 and 2
	$					# end of string
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
	"aaa#", 	# no (rule 2)
	"a", 		# no (rule 1)
]

for t in tests:
	validate_name(t)