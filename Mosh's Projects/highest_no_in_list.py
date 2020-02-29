# Grestest no. in list

numbers = ['2', '5', '6', '8', '94']
highest = numbers[0]
for number in numbers:
    if number > highest:
        highest = number
print(highest)
