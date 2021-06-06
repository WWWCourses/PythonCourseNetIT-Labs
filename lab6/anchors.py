import re


# regex = re.compile(r"(?m)^#.+");
# str = """
# #ta
# #ta
# #ta
# """

# results = regex.findall(str)

# print(results)



# phones = [
# 	"+359 88 1234567", # OK
# 	"jdjdkds : +359 88 1234567", # not OK
# 	"+359 88 1234567 this is my phone" # not ok
# ]
# regex = re.compile(r"^\+359 ?8[7-9] ?[0-9]{7}$")

# for ph in phones:
# 	print( regex.search(ph) )



regex = re.compile(r"\w")