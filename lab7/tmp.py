import re

# match only next words: "cat", "cats", "dog", "dogs" and nothing else:
strings = [
	"I love cats",
	"I love the dog!",
	"I love camels",
	"I love wildcats",
	"I love catalogs",
]
regex = re.compile(r"\b(:?cat|dog)s?\b")

for s in strings:
	match = regex.search(s)
	if match:
		print(f"'{s}' matched: {match[0]}")
	else:
		print(f"'{s}' did not match!")