""" **************************************************************************
    Reduce Function

    it takes a function and a sequence then reduces the sequence
    to a single value by repeatedly calling the function.
****************************************************************************** """

import functools


def calc_values(x, y: int):
    return x + y


numbers = [2, 4, 6, 5, 7, 23]

reduced_values = functools.reduce(calc_values, numbers)
print(reduced_values)
