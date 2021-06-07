import pytest
from src import find_next_symbol

@pytest.fixture
def simple_eq():
    return "1+2*3/4-5"

@pytest.fixture
def complex_eq():
    return "1+2+3-4-5-6*7*8*9/10/11/12"

@pytest.mark.find_next_symbol
@pytest.parametrize("symbol", ["+", "-", "/", "*"])
def test_simple_positive_case(symbol, simple_eq):
    index = find_next_symbol(simple_eq, symbol, 0)
    assert index == eq.find(symbol)

@pytest.mark.find_next_symbol
@pytest.parametrize("symbol", ["^", "%"])
def test_simple_negative_case(symbol, simple_eq):
    index = find_next_symbol(simple_eq, symbol, 0)
    assert index == None

@pytest.mark.find_next_symbol
@pytest.parametrize("symbol", ["+", "-", "/", "*"])
def test_repeated_symbol(symbol, complex_eq):
    offset = 0
    index = find_next_symbol(simple_eq, symbol, offset)

    while index != None:
        assert index == eq.find(symbol, offset)
        offset = index
        index = find_next_symbol(simple_eq, symbol, offset)
