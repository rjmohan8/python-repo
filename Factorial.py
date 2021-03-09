def fact_pgm():
    result = 1

    num = int(input('Enter num for factorial: '))

    while num > 1 and num != 0 and num != 1:
        if num == 0:
            print("0")
            break
        elif num == 1:
            print("1")

        result = result * num
        num -= 1

    print(result)

fact_pgm()











