class A:
	def __init__(self):
		self.a=1
		self.b=2

	def foo(self, attr_name):
		print(self.a)
		val = getattr(self,attr_name)
		print(val)



obj = A()
obj.foo('a')


