import pytest
numbers = [
    (2,True),
    (4,True)
]
def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False
@pytest.mark.parametrize('a,b',numbers)
def test_even(a,b):
    assert is_even(a) == b


