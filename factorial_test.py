import pytest
import factorial

def test_factorial():
    assert factorial.factorial(10) == 3628800
    assert factorial.factorial(0) == 1
    assert factorial.factorial(1) == 1
    assert factorial.factorial(2) == 2
    assert factorial.factorial(3) == 6

def test_partial_factorial():
    assert factorial.factorial(10, 9) == 90
    assert factorial.factorial(3, 1) == 6
    assert factorial.factorial(3, 2) == 6
    assert factorial.factorial(3, 3) == 3
