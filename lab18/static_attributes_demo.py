# name ="B"

class A:
	name="A"

	def __init__(self):
		# self.name = "obj"
		pass





obj1=A()
obj2=A()

print(obj1.name)
print(A.name)

# A.name = "Pesho"
obj1.name = "Pesho"
print(A.name)
print(obj1.name)
