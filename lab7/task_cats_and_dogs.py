import re

# match only next words: "cat", "cats", "dog", "dogs" and nothing else:
strings = [
	"I love cats",   # yes
	"I love cats!",   # yes
	"I love my cat!",   # yes
	"I love the dog!", # yes
	"I love camels", # no
	"I love wildcats", # no
	"I love catssssss!",   # no
	"I love catalogs", #no
]


# regex = re.compile(r"\b(cat|cats|dog|dogs)\b")
regex = re.compile(r"\b(?:cat|dog)s?\b")


# regex = re.compile(r"\bdog\b")
# regex = re.compile(r"\bdogs\b")

for s in strings:
	match = regex.search(s)
	if match:
		print(f"'{s}' matched: {match[0]}")
	else:
		print(f"'{s}' did not match!")