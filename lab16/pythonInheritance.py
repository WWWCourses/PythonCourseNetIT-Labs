# base class:
class Person():
	def __init__(self,name):
		self.name = name

	def greet(self):
		print(f'Hi I\'m {self.name}')

pesho = Person('Petar')
pesho.greet()


# derived class
class Student(Person):
	def __init__(self, name):
		super().__init__(name)




maria = Student('Maria')
maria.greet()
