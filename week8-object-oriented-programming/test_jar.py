from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(1)
    assert str(jar) == '🍪'
    jar.deposit(11)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1


def test_withdrawa():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.size == 1