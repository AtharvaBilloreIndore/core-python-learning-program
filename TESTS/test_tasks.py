from Tasks import add, difference, product, division
import pytest

def test_add():
    assert add(3, 4) == 7
    assert add(v, 5) == ValueError

def test_difference():
    assert difference(10, 5) == 5
    assert difference(g, 5) == ValueErrorpytest

def test_product():
    assert product(4, 5) == 20
    assert product(k, 5) == ValueError

def test_division():
    assert division(10, 2) == 5
    assert division(a,5) == ValueError