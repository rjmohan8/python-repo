def fact(n):
    res = 1

    if n == 0:
        return 0

    while n >= 1:
        res = res * n
        n = n - 1
    return res


val = int(input("Enter a value to find its factorial: "))
result=fact(val)
print(result)











