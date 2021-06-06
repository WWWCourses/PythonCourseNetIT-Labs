import re


# regex = re.compile(r"[aieyou]",re.I|re.M)
regex = re.compile("""(?sx)
.+ # this match every sumbol""")

str = """
'''TEST
this function 2 {}does something
'''
"""

m = regex.search(str)
print(m.group(0))