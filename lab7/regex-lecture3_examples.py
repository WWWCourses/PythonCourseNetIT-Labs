import re

def test_regex(regex,strings):
	for s in strings:
		match = regex.search(s)
		if match:
			print(f"'{s}' matched: {match[0]}")
		else:
			print(f"'{s}' did not match!")

# ---------------------------------------------------------------------------- #
#                                  Alternation                                 #
# ---------------------------------------------------------------------------- #
# --------------------------------- example 1 -------------------------------- #
# Match strings containg "cat" or "dog"
strings = [
	"1. I love cats and dogs",
	"2. I love dogs",
	"3. I love camels",
	"4. I love wildcats"
]
regex = re.compile(r"cat|dog")
# regex = re.compile(r"ca(t|d)og")

# test_regex(regex,strings)


# ---------------------------------------------------------------------------- #
#                                   Grouping                                   #
# ---------------------------------------------------------------------------- #
# --------------------------------- example 1 -------------------------------- #
# Match only words "strawberries" or "raspberries"
strings = [
	'Icecream with strawberries? Yes!',
	'Icecream with straws? No!',
	'Icecream with blueberries? No!',
	'Icecream with raspberries? Yes!',
	'Icecream with berries? No!',
]
regex = re.compile(r"\b(straw|rasp)berries\b")

# test_regex(regex, strings)


# --------------------------------- example 2 -------------------------------- #
# match only next words: "cat", "cats", "dog", "dogs" and nothing else:
strings = [
	"I love cats",
	"I love the dog!",
	"I love camels",
	"I love wildcats",
	"I love catalogs",
]
regex = re.compile(r"\b(?:cat|dog)s?\b")

# test_regex(regex,strings)

# --------------------------------- example 3 -------------------------------- #
# match only strings which contains only sequences of a letter (a-z) followed by digit:
strings = [
	"a1_b3b4",
	"a1b2c3a4",
	"ab1ab2ab3"
]
regex = re.compile(r"^(?:[a-z]\d)+$")

# test_regex(regex,strings)


# ---------------------------------------------------------------------------- #
#                         Capturing and back-reference                         #
# ---------------------------------------------------------------------------- #
# --------------------------------- example 1 -------------------------------- #
# match only strings starting with letter (a-z) and ending with the same letter
strings = [
	"a123a",
	"a123ab",
	"caaac"
]
regex = re.compile(r"^(\w).+\1$")

# test_regex(regex,strings)

# --------------------------------- example 2 -------------------------------- #
# match strings which contains only two repeated words. Between them are allowed
# only whitespaces, dots,"!" and ","
strings = [
	"echo echo",
	"echo echoooooo",
	"oh oh oh,oh",
]
regex = re.compile(r"^(\w+)[\s.!,]+\1$")

# test_regex(regex,strings)


# ---------------------------------------------------------------------------- #
#                               Capturing Groups                               #
# ---------------------------------------------------------------------------- #
# --------------------------------- example 1 -------------------------------- #
string = "1.234 56.78"
regex = re.compile('((\d+)\.(\d{2}))')


match = regex.match(string)

if match:
	print("match.group(1):", match.group(1))
	print("match.group(2):", match.group(2))
	print("match.group(3):", match.group(3))

	print("match[1]:", match[1])
	print("match[2]:", match[2])
	print("match[3]:", match[3])

	print("match.groups():", match.groups())
else:
	print("No match!")

# prints captured group 2 for all occurrences, not just first:
# for m in regex.findall(string):
# 	print(m[2])