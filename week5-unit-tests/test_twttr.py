import pytest
from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_lowercase_vowels():
    assert shorten("caeious50") == "cs50"

def test_uppercase():
    assert shorten("twIttEr") == "twttr"

def test_punctuation():
    assert shorten("cs.50") == "cs.50"
