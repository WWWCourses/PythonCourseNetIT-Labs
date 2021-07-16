class Base:
	def __init__(self, *args, **kwargs) :
		print(kwargs['windowTitle'])
		print(f'args in Base: {args}')

class Child(Base):
	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)

child1 = Child(2,3, windowTitle = "test")