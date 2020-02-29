x = int(input())
y = int(input())
z = int(input())
n = int(input())
pos_co = []
sum_co = 0
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                pos_co.append([])
                pos_co[sum_co] = [i, j, k]
                sum_co += 1
print(pos_co)
