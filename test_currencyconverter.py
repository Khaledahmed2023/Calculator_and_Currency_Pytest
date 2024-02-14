import pytest
from app.calculator import *
from app.currencyconverter import *

@pytest.mark.main
def test_crown_to_euro():   
    converter = CurrencyConverter(10,0)
    result = converter.crown_to_euro()
    assert result == 1.075


@pytest.mark.main
def test_euro_to_crown():
    converter = CurrencyConverter(100,0)
    result = converter.crown_to_euro()
    assert result == 10.75


