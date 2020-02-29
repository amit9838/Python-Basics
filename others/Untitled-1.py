def check(string):
    alphabets = ['abcdefghijklmnopqrstuvwxyz']
    new = []
    for x in string:
        if x[0] in alphabets:
            new.append(x)
        if new == alphabets:
            return True
        else:
            return False
        print(new)

check("The quick brown fox jumps over the lazy dog")