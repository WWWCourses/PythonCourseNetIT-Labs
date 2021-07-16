class Person:
	# static attribute
	counter = 0

	@staticmethod
	def count():
		Person.counter+=1

	def __init__(self, name, age):
		print(self)
		self.name = name
		self.age = age
		Person.count()


	def greet(self):
		print(self)

	def __str__(self):
		return f'{self.name} - {self.age}'

class Male:
	pass

class Student(Person,Male):
	def __init__(self, name, age, faculty):
		super().__init__(name, age)
		self.faculty = faculty

	def greet(self):
		pass


pesho1 = Person('Petyr1',41)

pesho2 = Person('Petyr2',42)
pesho3 = Person('Petyr3',43)
print(Person.count)


exit()

print(pesho)

maria = Student('Petyr', 23, 'Maths')

# maria.greet()
# 'Petyr - 23, Student in Maths