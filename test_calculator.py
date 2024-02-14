import pytest
from app.calculator import *

@pytest.mark.others
def test_add():
    calc = Calculator()
    result = calc.add(1,2)
    assert result == 3

@pytest.mark.others
def test_subtract():
    calc = Calculator()
    result = calc.subtract(8, 5)
    assert result == 3

@pytest.mark.others
def test_multiply():
    calc = Calculator()
    result = calc.multiply(3,1)
    assert result == 3

@pytest.mark.others
def test_divide():
    calc = Calculator()
    result = calc.divide(6,3)
    assert result == 2