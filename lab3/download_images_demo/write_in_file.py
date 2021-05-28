# write in file "test.txt" the string "test"

thing_to_write = "test"

with open("test.txt","w") as fh:
	fh.write(thing_to_write)
