def cub(x):
	# print(f"{x**3}")
	return x**3

l =[1,2,3,4]
cub_l = map(cub,l )

print(list(cub_l))
# for el in l:
# 	cub(el)