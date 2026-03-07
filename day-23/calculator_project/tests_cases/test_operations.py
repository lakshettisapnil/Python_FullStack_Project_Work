import pytest
from calculator.operations import add, sub, mul, div 
#---------------add tests 8------------------
def test_add_positive():
    assert add(2,3) == 5
def test_add_negative():
    assert add(-2,-3) == -5
def test_add_mixed():
    assert add(-2,3) == 1
def test_add_zero():
    assert add(0,5) == 5
def test_add_large(a,b):
    assert add(100000,200000) == 300000
