cmd = input()
x=0
y=0
for item in cmd:
    if item == "L":
        x-=1
    elif item =="R":
        x+=1
    elif item =="U":
        y+=1
    elif item == "D":
        y-=1
    

print(x,y)