class Iter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.start, self.stop):
            self.start += 1
            return chr(i)
        raise StopIteration


chars = Iter(65, 91)
for c in chars:
    print(c)
