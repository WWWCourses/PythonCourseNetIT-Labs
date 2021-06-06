import re

# # aieouy
# pattern = r"[aieouy]"
# strings = [
# 	"trttrt", # no
# 	"test",   # yes
# ]

# for str in strings:
# 	print( re.search(pattern,str))


def match_bg_mobile_numbers(number):
	pattern = r"\+359 ?8[7-9] ?[0-9]{7}"
	print( re.search(pattern, number) )

# match_bg_mobile_numbers("+35986 1234567")

digit = re.compile(r"[0-9]")
word_char = re.compile(r"[0-9][a-z][A-Z]_-")



digit_class = re.compile(r"\w")
word_char_class = re.compile(r"[\w-]")





