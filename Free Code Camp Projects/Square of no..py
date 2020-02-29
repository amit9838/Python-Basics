squares = []
for x in range(2, 11):
    squares.append(x**2)
print(squares)
squares.pop()  # Removing last item from list.
print(squares)
squares.pop(0)  # removing element with index 0 i.e. first element of the list.
print(squares)

squares.clear()
for x in range(10, 20, 2):  # This gives list [10,12,14,16,18,20]
    squares.append(x**2)
print(squares)
print(squares.index(144))
print(squares.sort(reverse=True))  # This operation is not valid for numerical data type.
