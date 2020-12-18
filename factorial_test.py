import pytest
from pytest_unordered import unordered
import factorial
import math

def test_factorial():
    assert factorial.factorial(10) == math.factorial(10) #3628800
    assert factorial.factorial(0) == 1
    assert factorial.factorial(1) == 1
    assert factorial.factorial(2) == 2
    assert factorial.factorial(3) == 6

def test_partial_factorial():
    assert factorial.factorial(10, 9) == 9 * 10
    assert factorial.factorial(3, 0) == 6
    assert factorial.factorial(3, 1) == 6
    assert factorial.factorial(3, 2) == 6
    assert factorial.factorial(3, 3) == 3
    assert factorial.factorial(5, 0) == 120
    assert factorial.factorial(10, 5) == 5 * 6 * 7 * 8  * 9 * 10
    assert factorial.factorial(6,4) == 4 * 5 * 6

def test_partial_factorial_sets():
    assert factorial.partial_factorial_sets(n=10, sets=1) == [(1, 10)]
    assert factorial.partial_factorial_sets(n=10, sets=2) == unordered([(6, 10), (1, 5)])
    # todo: uneven sets

def test_integrate_sets_and_factorial_10():
    result = 1
    for first, last in factorial.partial_factorial_sets(n=10, sets=2):
        temp = factorial.factorial(first=first, last=last)
        print("{} {} {}".format(first, last, temp))
        result = result * temp
    assert result == math.factorial(10) #3628800 # 10!
