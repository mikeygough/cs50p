from plates import is_valid

def test_beginning_alphabetical():
    assert is_valid("11") == False

def test_alphabetical():
    assert is_valid("CS50") == True

def test_length_7():
    assert is_valid("ECTO888") == False

def test_length_1():
    assert is_valid("H") == False

def test_number_placement():
    assert is_valid("AAA22A") == False

def test_zero_placement_beginning():
    assert is_valid("0AA022") == False

def test_zero_placement_CS05():
    assert is_valid("CS05") == False

def test_alphanumeric_characters():
    assert is_valid("CS50.") == False

