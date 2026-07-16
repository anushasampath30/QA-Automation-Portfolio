import pytest
def test_one_plus_one():
    assert 1+1 == 2

def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert "division by zero" in str(e.value)

products = [
    (3,3,9),
    (1,99,99),
    (0,99,0)
]
@pytest.mark.parametrize('a,b,product',products)
def test_multiply(a,b,product):
    assert a * b == product