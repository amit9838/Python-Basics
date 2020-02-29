string = input()
x = 0
y = 0
for item in string:
    if item == "z":
        x += 1
    elif item == "o":
        y += 1

if x*2 == y:
    print("Yes")
else:
    print("No")