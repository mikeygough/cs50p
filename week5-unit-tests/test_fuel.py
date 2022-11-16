import pytest

from fuel import convert
from fuel import gauge

def test_single_str():
    with pytest.raises(ValueError):
        convert("cat")

def test_double_str():
    with pytest.raises(ValueError):
        convert("three/four")

def test_str_int():
    with pytest.raises(ValueError):
        convert("one/2")

def test_float_num():
    with pytest.raises(ValueError):
        convert("1.5/3")

def test_x_greater_y():
    with pytest.raises(ValueError):
        convert("2/1")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_e():
    assert gauge(1) == "E"

def test_f():
    assert gauge(99) == "F"

def test_percent():
    assert gauge(50) == "50%"

def test_convert():
    assert convert("1/2") == 50