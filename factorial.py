def factorial(end, start=1):
    # expected n >= 0
    result = 1
    for i in range(start,end+1):
        result = result * i
    return result
