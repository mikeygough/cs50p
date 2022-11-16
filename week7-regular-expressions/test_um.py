# test file
import pytest
from um import count


def test_single():
    assert count('um') == 1


def test_sentence():
    assert count('hello, um, world.') == 1


def test_multiple():
    assert count('um, hello, um, world') == 2


def test_in_word():
    assert count('she enjoys summo wrestling and blueberry gum') == 0


def test_uppercase():
    assert count("UM...") == 1