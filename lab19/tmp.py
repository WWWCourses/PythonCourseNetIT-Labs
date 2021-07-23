# find the squares of the first ten natural numbers and print the sum of the squares

squares = []

for i in range(1, 11):
    square = i**2
    squares.append(square)

print(squares)
print(sum(squares))