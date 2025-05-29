from Tasks import add, difference, product, division
import pytest

def test_add():
    assert add(3, 4) == 7
    
def test_add_string_input():
    with pytest.raises(TypeError):
        add("a",96)
        
def test_difference():
    assert difference(10, 5) == 5
    
def test_difference_string_input():
    with pytest.raises(TypeError):
        difference("d",35)
    
def test_product():
    assert product(4, 5) == 20

def test_profuct_string_input():
    with pytest.raises(TypeError):
        add("l",57)

def test_division():
    assert division(10, 2) == 5

def test_division_string_input():
    with pytest.raises(TypeError):
        add("x",78)
