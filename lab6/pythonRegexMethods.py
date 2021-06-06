import re



# m = re.search(r"\+", "find in me the +")

# regex = re.compile(r"\+359")
# m = regex.match("find in me the +359 sign +")

# print(m.group())
# print(m[0])


regex = re.compile(r"[aieouy]")
str = "as is that"

m=regex.findall(str)
print(m)