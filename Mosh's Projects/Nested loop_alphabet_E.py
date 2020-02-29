      #Nested loop
#Improper Method
numbers=[5,2,5,2,5]
count=0
for count in numbers:
    print('x'*count)

print("""

With proper Method
""")
    
#Proper Method
numbers=[5,2,5,2,5]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output+='x'
    print(output)
