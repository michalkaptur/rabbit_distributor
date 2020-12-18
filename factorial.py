def factorial(last, first=1):
    # expected n >= 0
    result = 1
    for i in range(first,last+1):
        result = result * i
    return result
