class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError('Deposit exceeds capacity')
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError('Withdrawal exceeds siz')
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('Capacity less than 0')
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError('Size cannot be greater than capacity')
        self._size = size