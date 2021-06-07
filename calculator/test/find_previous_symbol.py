import pytest
from src import find_previous_symbol

@pytest.fixture
def simple_eq():
    return "1+2*3/4-5"

@pytest.fixture
def complex_eq():
    return "1+2+3-4-5-6*7*8*9/10/11/12"

@pytest.mark.find_previous_symbol
def test_simple_positive_case(simple_eq):
    index = find_previous_symbol(simple_eq, 2)
    assert index == 1

@pytest.mark.find_previous_symbol
@pytest.parametrize("symbol", ["^", "%"])
def test_simple_negative_case(symbol, simple_eq):
    index = find_previous_symbol(simple_eq, 0)
    assert index == None

@pytest.mark.find_previous_symbol
@pytest.parametrize("symbol", ["+", "-", "/", "*"])
def test_repeated_symbol(symbol, complex_eq):
    offset = len(complex_ex)-1
    total_found = 0
    index = find_previous_symbol(simple_eq, offset)

    while index != None:
        total_found += 1
        offset = index
        index = find_previous_symbol(simple_eq, offset)

    assert total_found == 11
