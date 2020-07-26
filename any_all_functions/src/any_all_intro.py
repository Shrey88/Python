""" ***************************************************************************
    Any / All function

    All : checks if the items in an iterable are true.

    Any : checks to see if any of them are true.

    both the functions takes and return true or false depending on the values
    in the iterable

    so what do you mean when we say true items or true values?
        0 is false
        None is false
        bool(0) is false
        bool(0.0) is false
        bool([]) is false   <-- empty list
        bool(()) is false   <-- empty tuple
        bool('') is false   <-- empty string
        bool("") is false   <-- empty string
        bool({}) is false   <-- empty mapping is false
******************************************************************************* """

entries = [1, 2, 3, 4, 5]

print("All : {}".format(all(entries)))  # <-- it returns true because all the value in the list are true

print("Any : {}".format(any(entries)))  # <-- it returns true because at least one value of them is true.

print('*' * 20)

entries = [0, 1, 2, 3, 4, 5]

print("All : {}".format(all(entries)))  # <-- it returns false because one of the item is not having the true value i.e. 0

print("Any : {}".format(any(entries)))  # <-- it returns true because at least one value of them is true.

print('*' * 20)

""" *
    *   so when you provide the empty list you will see some strange return value
    * """
empty_list = []


print("All : {}".format(all(empty_list)))  # <-- it returns true, this is the documented behaviour

# so to overcome the first problem you can do if-else condition check
if empty_list:
    print("All : {}".format(all(empty_list)))
else:
    print("All : {}".format(False))


print("Any : {}".format(any(empty_list)))  # <-- this returns the false as there are no true value or items



