import pytest 
from calculator.operations import add, sub, mul, div
def test_add_positive():
    assert add(2,3) == 5
def test_add_negative():
    assert add(-2,-3) == -5
def test_add_mixed():
    assert add(-2,3) == 1
def test_add_zero():
    assert add(0,5) == 5
def test_add_large():
    assert add(100000,200000) == 300000
def test_add_float():
    assert add(2.5,2.5) == 5
def test_add_zero_zero():
    assert add(0,0) == 0
#-------------------sub------------
def test_subtract_positive():
    assert sub(10,5) == 5
def test_subtract_negative():
    assert sub(-10,-5) == -5
def test_subtract_mixed():
    assert sub(-10,5) == -15
def test_subtract_zero():
    assert sub(10,0) == 10
def test_subtract_large():
    assert sub(500000, 200000) == 300000
def test_subtract_float():
    assert sub(5.5, 2.5) == 3.0
def test_subtract_equal():
    assert sub(5,5) == 0
#-----------------mul---------------------
def test_multiply_positive():
    assert mul(2,3) == 6
def test_multiply_negative():
    assert mul(-2,-3) == 6
def test_multiply_mixed():
    assert mul(-2,3) == -6
def test_multiply_zero():
    assert mul(2,0) == 0
def test_multiply_large():
    assert mul(2000, 3000) == 6000
def test_multiply_float():
    assert mul(2.5, 2) == 5.0
def test_multiply_one():
    assert mul(5,1) == 5
#-----------------div--------------
def test_divide_positive():
    assert div(10,2) == 5
def test_divide_negative():
    assert div(-10,-2) == 5
def test_divide_mixed():
    assert div(-10,2) == -5
def test_divide_float():
    assert div(5,2) == 2.5
def test_divide_one():
    assert div(10,1) == 10
def test_divide_large():
    assert div(1000000,1000) == 1000
def test_divide_numerator():
    assert div(0,5) == 0
def test_divide_by_zero():
    with pytest.raises(ValueError):
        div(10,0)
