print("ax^2 + bx + c")
print("Enter the value of coeffecients:")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

x1 = (-b+((b**2)-(4*a*c))**.5)/2*a
x2 = (-b-((b**2)-(4*a*c))**.5)/2*a
print(f"x = {x1},{x2}")