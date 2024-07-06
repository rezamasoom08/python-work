def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

a = int(input("Enter a value: "))
print(a)
result = factorial(a)
print(result)