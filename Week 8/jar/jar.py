class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Only non-negative number")
        self._capacity = capacity
        self.jar = 0

    def __str__(self):
        return "🍪" * self.jar

    def deposit(self, n):
        if self.jar + n > self._capacity:
            raise ValueError("Beyond jar capacity")
        else:
            self.jar += n

        return self.jar

    def withdraw(self, n):
        if n > self.jar:
            raise ValueError("Not enough cookies")
        else:
            self.jar -= n

        return self.jar

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.jar
