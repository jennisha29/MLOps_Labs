import pytest
from src import calculator


def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5, 0) == 5
    assert calculator.fun1(-1, 1) == 0
    assert calculator.fun1(-1, -1) == -2

    with pytest.raises(ValueError):
        calculator.fun1("2", 3)
    with pytest.raises(ValueError):
        calculator.fun1(2, None)

def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5, 0) == 5
    assert calculator.fun2(-1, 1) == -2
    assert calculator.fun2(-1, -1) == 0

    with pytest.raises(ValueError):
        calculator.fun2("2", 3)
    with pytest.raises(ValueError):
        calculator.fun2(2, [])

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5, 0) == 0
    assert calculator.fun3(-1, 1) == -1
    assert calculator.fun3(-1, -1) == 1

    with pytest.raises(ValueError):
        calculator.fun3("2", 3)
    with pytest.raises(ValueError):
        calculator.fun3(2, {})

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5, 0, -1) == 4
    assert calculator.fun4(-1, -1, -1) == -3
    assert calculator.fun4(-1, -1, 100) == 98

    with pytest.raises(ValueError):
        calculator.fun4(1, 2, "3")
    with pytest.raises(ValueError):
        calculator.fun4(1, None, 3)

def test_fun5():
    assert calculator.fun5(2, 3) == 8
    assert calculator.fun5(5, 0) == 1
    assert calculator.fun5(-2, 2) == 4

    with pytest.raises(ValueError):
        calculator.fun5("2", 3)
    with pytest.raises(ValueError):
        calculator.fun5(2, "3")

def test_fun6():
    assert calculator.fun6(0) == 1
    assert calculator.fun6(1) == 1
    assert calculator.fun6(5) == 120

    with pytest.raises(ValueError):
        calculator.fun6(-1)
    with pytest.raises(ValueError):
        calculator.fun6(2.5)
    with pytest.raises(ValueError):
        calculator.fun6("5")

def test_fun7():
    assert calculator.fun7(10, 3) == 10
    assert calculator.fun7(-1, 1) == 1
    assert calculator.fun7(5, 5) == 5

    with pytest.raises(ValueError):
        calculator.fun7("10", 3)
    with pytest.raises(ValueError):
        calculator.fun7(10, None)

def test_fun8():
    assert calculator.fun8(6) is True
    assert calculator.fun8(7) is False
    assert calculator.fun8(0) is True
    assert calculator.fun8(-2) is True

    with pytest.raises(ValueError):
        calculator.fun8(2.0)
    with pytest.raises(ValueError):
        calculator.fun8("6")

def test_fun9():
    assert calculator.fun9(0) == 0.0
    assert calculator.fun9(9) == 3.0
    assert calculator.fun9(2.25) == 1.5

    with pytest.raises(ValueError):
        calculator.fun9(-1)
    with pytest.raises(ValueError):
        calculator.fun9("9")