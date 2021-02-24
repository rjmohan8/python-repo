def fibo_series(num):

    first = 0
    second = 1
    result_arr = []
    """result.append(first)
    result.append(second)"""

    for item in range(num):
        result = first+second
        first = second
        second = result
        result_arr.append(result)
        #result_arr.append(second)

    return result_arr


res = fibo_series(10)

print(res)

