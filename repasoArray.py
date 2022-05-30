import random

class Array:
    def __init__(self, n : int, value = None):
        self.items = []
        for i in range(n):
            self.items.append(value)


    def __getitem__(self, item):
        return self.items[item]

    def __setitem__(self, key, newValue):
        self.items[key] = newValue

    def __iter__(self):
        return iter(self.items)

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def generateRandom(self):
        for i in range(len(self.items)):
            self.items[i] = random.randint(0, 100)

    def sumValues(self):
        return sum(self.items)
