import re

# TASK: validate user email
# "<atleast 3 symbols>@<at least 1 letter>.<at least 3 letters>"
user_mail = "alabala@test.com"

# str = ">\\t<";
# r_str = r">\t<"
# print(str);
# print(r_str);

#special regex character
# . , + , * , ? , ^ , $ , ( , ) , [ , ] , { , } , | ,

# TODO: check r"\c" => error
pattern = r"1aaa1";
str_to_search = "1aaa1"




if re.search(pattern, str_to_search):
	print("Match")
else:
	print("no Match")
