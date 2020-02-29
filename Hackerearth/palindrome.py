string = input()
string.lower()
rev = string[::-1]
if rev == string:
    print("YES")
else:
    print("NO")
