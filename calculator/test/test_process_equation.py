import pytest
from src import process_operation

@pytest.fixture
def simple_eq():
    return "1+2*3/4-5"

@pytest.fixture
def complex_eq():
    return "1+2+3-4-5-6*7*8*9/10/11/12"
