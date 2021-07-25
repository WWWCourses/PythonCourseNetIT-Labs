def caller(f,x,y):
	print(x,y)
	res = f()
	return res ** 2

def callback():
	# print(f'x,y in callback: {x},{y}')
	return 5;

add1 = caller(callback, 2,3)
add = caller( lambda:5, 1,2)
print(add)