def say_hi(name, age):
    print("Hello " + name + ", You are " + age)


print("Top")
say_hi("Amit", "20")  # Calling function 'say_hi'
say_hi("Abhishek", '22')  #    //
print("Bottom")


def sq(num):
    result =num*num
    print(f'Square of {num} is {result}')
    return result

ans = sq(3)
print(ans)