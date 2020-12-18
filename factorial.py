def factorial(n):
    # expected n >= 0
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result
