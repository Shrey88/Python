# iterator is an object that represents stream of data
# it actually returns the stream or actual data in stream , one element at a time .
# strings and list are 2 iterable objects.

string = "0123456789"

# my_iterator = iter(string)
# # gives the memory location of string
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
#
# # Code Terminates as we have already reached
# # the end of the string and there is nothing to print
# print(next(my_iterator))

# here in this case for loop is implicitly creating the iterator for iterable object of string.
for char in string:
    print(char)

print()

# this is similar to above version of for loop
# so this is how for loop in above case creates the iterator for the iterable object implicitly
for char in iter(string):
    print(char)

