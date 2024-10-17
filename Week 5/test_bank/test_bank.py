from bank import value


def test_hello():
    assert value("hello cs50") == 0
    assert value("HELLO CS50") == 0


def test_h():
    assert value("hi") == 20
    assert value("Hi") == 20


def test_any():
    assert value("good morning") == 100
    assert value("Good Morning") == 100
