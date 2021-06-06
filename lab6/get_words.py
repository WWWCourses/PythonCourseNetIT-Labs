import re

# word is at least 1 symbol of ' a-z A-Z 0-9 _ -
sentance = "this,is a very long string! The-best!"

regex = re.compile(r"[\w-]+")
word_list = regex.findall(sentance)

print(word_list)