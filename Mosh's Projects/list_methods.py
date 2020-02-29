#List methods
numbers=[2,4,3,6,5]
print(numbers)
numbers.append(20) #"___.append" method adds an item at the end of the list.
print(numbers)
numbers.insert(0,12) # To insert an item at given index(0) with given value(12). And all other items wil be pushed forward.
print(numbers)
numbers.remove(3) #To remove an item with given value(3).
print(numbers)
# numbers.clear()  #This will remove all the items present in the list.
numbers.pop() #This will remove the last item from the list.
print(numbers)
print(numbers.index(6)) #This will give the index if given value(6).

              #To check the existance of a number
#Wrong method. gives an error to the sys.
# print(numbers.index(9))
#Right method
print(9 in numbers)
print(12 in numbers)
numbers.sort() #To sort the numbesr in ascending order.
print(numbers)
numbers.reverse() #To sort the numbesr in descending order.
print(numbers)
#Sorting method dosen't affect the original list. Actually it creates a new list.





