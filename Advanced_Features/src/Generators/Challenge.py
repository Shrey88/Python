""" =======================================================================
    Challenge: creator a generator to return an infinite sequence of add numbers, starting at 1

    Print first 100 numbers, to check that the generators' working correctly.

=========================================================================== """
def odd_no_generator():
    start = 1
    while start > 0:
        if start % 2 != 0:
            yield start
        start += 1


for i in odd_no_generator():
    print(i)