lucky_numbers = [2, 4, 5, 6, 7, 13]
friends = ['John', 'Roy', 'Tanish', 'Robert']
friends2 = friends.copy()
friends.extend(lucky_numbers)  # Adding two lists.
print(friends)

lucky_numbers.extend(friends)
print(lucky_numbers)

print(friends2)
print(friends2.pop())
print(friends2)
friends2.insert(1, 'Rohan')
print(friends2)
friends2.remove('Rohan')
print(friends2)
print(friends2.index('Tanish'))
# print(is 'Roy' in friends2)