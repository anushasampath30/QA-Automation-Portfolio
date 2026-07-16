import pytest
from module_1.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()

def test_count_init(accum):
    assert accum.count == 0

def test_add(accum):
    accum.add(3)
    assert accum.count == 3
