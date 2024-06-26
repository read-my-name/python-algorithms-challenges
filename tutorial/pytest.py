# test_my_module.py
from my_module import add

def test_add_integers():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2

def test_add_floats():
    assert add(1.5, 2.5) == 4.0
    assert add(-1.1, -1.1) == -2.2

def test_add_strings():
    assert add('hello', ' world') == 'hello world'
