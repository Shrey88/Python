""" *
    *
    * """
import itertools

""" ===================================================================
    Infinite iterators
======================================================================= """

""" *
    * Cycle :   it cycles over a set of values
    * """
seq1 = ["Joe", "John", "Mike"]
cycle1 = itertools.cycle(seq1)
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))  # <-- at this point the iterator will start over again from the start

print()
""" *
    * Count :   it takes the start value and step value
    * """
count1 = itertools.count(100, 10)  # starting value is 100 and it will step by 10
print(next(count1))
print(next(count1))
print(next(count1))
print(next(count1))
print(next(count1))

print()
""" *
    *   Accumulate  :   it generates the running addition of numbers that came before
    *   
    *   0th index   :   vals[0]
    *   1st index   :   vals[0] + vals[1]
    *   2nd index   :   vals[0] + vals[1] + vals[2] and so on 
    * """
vals = [10, 20, 30, 40, 50, 40, 30]
acc = itertools.accumulate(vals)
print(acc)  # <-- it is the object of type itertools.accumulate
print(list(acc))

""" *   the behaviour can be changed by providing different function for accumulation
    *   max is the in-built function
    *   so it will find the highest no from the list and keeps providing 
    *   the same value unless there is no highest no in list
    * """
acc = itertools.accumulate(vals, max)

print()

""" *
    *   Chain   :   it will take multiple sequences and chain them together to act as one
    * """
x = itertools.chain("ABCD", "1234")
print(list(x))

print()

""" *   these two functions are similar to filter functions so these iterator will
    *   provide  values until a trigger value is reached at which point they will stop
    *
    *   DropWhile   :   these will drop values from the function
    *                   while the test function returns true and then it will start
    *                   returning every value after that
    *
    *   TakeWhile   :   it will return values from the seq while the predicate function return true and then 
    *                   it will stop giving you values
    * """
def testfunction(x):
    return x < 40

""" *
    *   so in this case since the first three values evaluates to trueand those values will be removed from the list
    * """
print(list(itertools.dropwhile(testfunction, vals)))

""" *
    *   so in this case since the first three values evaluates to true and those values will be added to the list
    * """
print(list(itertools.takewhile(testfunction, vals)))