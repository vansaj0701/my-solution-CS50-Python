from plates import is_valid


def test_valid():
    assert is_valid("HELLO") == True
    assert is_valid("CS50") == True


def test_invalid():
    assert is_valid("AB.C#D") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("CS05") == False
    assert is_valid("1234") == False
    assert is_valid("0CS5") == False
    assert is_valid("CS50P") == False
