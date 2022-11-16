from bank import value

def test_lowercase_hello():
    assert value("hello") == 0

def test_lowercase_hey():
    assert value("hey") == 20

def test_lowercase_yo():
    assert value("yo") == 100

def test_uppercase_hello():
    assert value("HELLO") == 0

def test_uppercase_hey():
    assert value("HEY") == 20

def test_uppercase_yo():
    assert value("YO") == 100

def test_phrase():
    assert value("Yo, man!") == 100