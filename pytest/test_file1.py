#showing off the assert and approx statements from pytest
import pytest

def test_1():
    assert 1 == 1

def test_2():
    assert 's' == 's'

def test_3():
    assert [1,2,3] == [1,2,3]

def test_4():
    assert {'a' : 1} == {'a' : 1}

#fails!
def test_5():
    assert (0.1 + 0.2) == 0.3

#doesn't (:
def test_6():
    assert (0.1 + 0.2) == pytest.approx(0.3)

