print("                DETERMINANT CALCULATOR")

print("       |a1   a2   a3|")
print("       |            |")
print("       |b1   b2   b3|")
print("       |            |")
print("       |c1   c2   c3|")
print("")
print("Enter Elenents of matrix:  ")
a1 = int(input("a1: "))
a2 = int(input("a2: "))
a3 = int(input("a3: "))
b1 = int(input("b1: "))
b2 = int(input("b2: "))
b3 = int(input("b3: "))
c1 = int(input("c1: "))
c2 = int(input("c2: "))
c3 = int(input("c1: "))
mat=[
    [a1,a2,a3],
    [b1,b2,b3],
    [c1,c2,c3]
]

print("Please wait...")
# for item in mat:
    # print(item)
D=(mat[0][0]*((mat[1][1]*mat[2][2])-(mat[2][1]*mat[1][2])))-(mat[0][1]*((mat[1][0]*mat[2][2])-(mat[2][0]*mat[1][2])))+(mat[0][2]*((mat[1][0]*mat[2][1])-(mat[2][0]*mat[1][1])))

print(f"       Determinant = {D}")
