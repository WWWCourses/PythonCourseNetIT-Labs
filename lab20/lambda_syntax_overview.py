# https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

# lambda with argumants and no return value (not a good practice)
def test(callback,*args):
	print('Doing some work here...')
	res =callback(*args)

test( lambda x,y: print(x+y), 1,2 )

# # lambda with argumants and return value
# def test(callback,*args):
# 	print('Doing some work here...')
# 	return callback(*args)

# res =test(lambda x,y: x+y, 1,2 )
# print(res)

# lambda without aruments and return value
foo = lambda:print('foo')
foo()