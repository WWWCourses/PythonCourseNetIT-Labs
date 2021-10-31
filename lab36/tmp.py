class Fruit:

	# name = 'Fruitas'

	def printName(self):
		print('Instance said:', self.name)

	@classmethod
	def printName(cls):
		print('class said:', cls.name)


apple = Fruit()
# apple.printName()

Fruit.printName(apple)

/^/ =