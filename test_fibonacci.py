import pytest
from fibonacci import fibonacci

def test_fibonacci_zero():
    assert fibonacci(0) == 0

def test_fibonacci_one():
    assert fibonacci(1) == 1

def test_fibonacci_two():
    assert fibonacci(2) == 1

def test_fibonacci_five():
    assert fibonacci(5) == 5

def test_fibonacci_ten():
    assert fibonacci(10) == 55

def test_fibonacci_negative_number():
    with pytest.raises(ValueError):
        fibonacci(-1)
