def factorial(last, first=1):
    # expected n >= 0
    first = max(first,1)
    result = 1
    for i in range(first,last+1):
        result = result * i
    return result

def partial_factorial_sets(n, sets):
    def ceil_div(a, b):
        return -(a // -b) #thanks SO
    set_capacity = ceil_div(n, sets)
    result = []
    for i in range(0, sets):
        result.append((i*set_capacity+1, (i+1)*set_capacity))
    return result