squares = []
for x in range(2, 11):
    squares.append(x**2)
print(squares)
#  OR
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

# OR

squares2 = [x ** 2 for x in range(8)]
print(squares2)
