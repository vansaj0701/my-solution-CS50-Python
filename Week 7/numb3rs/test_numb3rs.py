from numb3rs import validate

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.2.3") == False
    assert validate("cat") == False
    assert validate("255.532.846.300") == False
