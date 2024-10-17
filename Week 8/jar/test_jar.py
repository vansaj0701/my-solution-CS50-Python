from jar import Jar
import pytest

jar = Jar(10)


def test_init():
    assert jar._capacity == 10


def test_str():
    jar.deposit(2)
    assert str(jar) == "🍪🍪"


def test_withdraw():
    jar.deposit(5)
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_capacity():
    assert jar.capacity == 10


def test_size():
    jar.deposit(5)
    assert jar.size == 10
