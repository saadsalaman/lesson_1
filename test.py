from main import add, subtract, multiply
import pytest
def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(1, -1) == 0

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(1, -1) == 2

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(0, 0) == 0
    assert multiply(-1, -1) == 1
    assert multiply(1, -1) == -1