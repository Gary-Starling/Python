import random

class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, x):
        self.x = x
        self.i = 0


    def __next__(self):
        if self.i < self.x:
            self.i += 1
            return random.random()
        else:
            raise StopIteration


for x in RandomIterator(10):
    print(x)