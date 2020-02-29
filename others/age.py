def fibonacci(n):
    list1 = []
    a = 0
    b = 1
    c = 0

    if n == 1:
        print(a)
    else:
        for i in range(2, n):
            while c < 4000000:
                c = a+b
                list1.append(c)
                a = b
                b = c
        print(list1)
        list2 = []
        for x in list1:
            if x % 2 == 0:
                list2.append(x)
        print(list2)
        even = 0
        for x in list2:
            even = even + x
        print(even)


fibonacci(32)
