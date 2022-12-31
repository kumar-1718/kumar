import pytest
from project import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(2, -3) == -1

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, 3) == -8
    assert subtract(5, -3) == 8

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(6, -3) == -2

def test_power():
    assert power(2, 3) == 8
    assert power(-2, 3) == -8
    assert power(2, -3) == 0.125

def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(2) == 1.4142135623730951

if __name__ == "__main__":
    pytest.main()
