class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self


fib = Fibonacci(20, 100)
for num in fib:  # iter() returned non-iterator of type 'Fibonacci'
    print(num)
