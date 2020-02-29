#List
names=['Ram', 'Shyam', 'Mohan', 'Aman', 'Ankit']
print(names)
print(names[0])    # 0 is counted as the first item of the list
print(names[-1])
print(names[-2])
print(names[2:4])
print(names[1:])   #in this case null value is counted as index of last item.
names[0]='Kisan'
print(names[0])
print(names[ :4])   #In this case null value is counted as index of first item.
names[0]='Lakshman'
print(names[0])
