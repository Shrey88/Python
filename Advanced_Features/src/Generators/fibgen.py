""" ================================================================
fibonacci Series
==================================================================== """

""" *
    *   so that's actually a generator that returns successive Fibonacci numbers each time we call next to get 
    *   the next value
    * """
def fibonacci():
    current, previous = (0,1)
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()

for i in range(21):
    print(next(fib))