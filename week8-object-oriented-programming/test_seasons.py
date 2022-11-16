import pytest
from seasons import convert

def test_one_year():
    assert convert("2021-10-25") == "Five hundred twenty-five thousand, six hundred minutes"

def test_two_years():
    assert convert("2020-10-25") == "One million, fifty-one thousand, two hundred minutes"