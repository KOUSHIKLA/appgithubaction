from src.math_operation import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    # Removed incorrect assertion, sub(5,3)==2 not 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(4, 5) == -1
    assert sub(9, 0) == 9
