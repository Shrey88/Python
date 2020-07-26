""" ===========================================================================
Generators save lot of memory
=============================================================================== """
import sys

""" *
    *   so here we are comparing the sizeof the variable depending on the type, the memory it is consuming
    *
    *   so both big_range and big_list are actually iterators, so we can use either in a for loop to iterate over all the values 
    *
    *   big_range is a special case of an iterator called a generator
    *"""
# big_range = range(100000)
#
# print("big_range is {} bytes".format(sys.getsizeof(big_range)))
#
# # create a list containing all the values in big_range
# big_list = []
# for val in big_range:
#     big_list.append(val)
#
# print("big_list is {} bytes".format(sys.getsizeof(big_list)))


""" *
    *   here we are creating our own generator, in the previous example we had an implicit generator and size of list was 
    *   more 
    *   but after creating our own generator the size of list is much smaller than using the implicit generator for getting 
    *   the values and storing it into the list.
    *   
    *   when it is a generator and uses yield it uses more memory
    *   
    * """
# def my_range(n: int):
#     print("my_range starts")
#     start = 0
#     while start < n:
#         """ *
#             *   if we use the return in place of yield then it gives us the error that int object is not iterable
#             *
#             *   but when we use yield the function actually returns the yielded value then goes into the suspended state
#             *   so it doesn't just return the value it keeps the track of all the its variable, so next time it's called
#             *   it wakes up and continues from where it left off.
#             * """
#         print("my_range is returning {}",format(start))
#         # return start
#         yield start
#         start += 1
#
#
# _ = input("line 51")
# big_range = my_range(5)  # at this point nothing is executed so use my_range directly in for loop
# _ = input("line 53")
#
# print("big_range is {} bytes".format(sys.getsizeof(big_range)))
#
# # create a list containing all the values in big_range
# big_list = []
# _ = input("line 59")
# for val in big_range:
#     _ = input("line 61")
#     big_list.append(val)
# _ = input("line 63")
#
# print("big_list is {} bytes".format(sys.getsizeof(big_list)))
#
# print(big_range)  # it will that it is a generator object
# print(big_list)


""" *
    *   so we are going to use the next instead of using it in for loop
    *   when you use the next keyword to actually execute the my_range function
    *
    * """
# def my_range(n: int):
#     print("my_range starts")
#     start = 0
#     while start < n:
#         print("my_range is returning {}",format(start))
#         yield start
#         start += 1
#
#
# """ note that this example also explains why is it a bad idea to assign a generator to a variable """
# big_range = my_range(5)  # at this point nothing is executed, so use my_range directly in for loop
# _ = input("line 87")
#
# print(next(big_range))  # the code is being executed here which yields the first value.
# print("big_range is {} bytes".format(sys.getsizeof(big_range)))
#
# # create a list containing all the values in big_range
# big_list = []
# _ = input("line 94")
# for val in big_range:  # here the for loop is calling the next to get us the next value.
#     _ = input("line 96")
#     big_list.append(val)
# _ = input("line 98")
#
# print("big_list is {} bytes".format(sys.getsizeof(big_list)))
#
# print(big_range)  # it will that it is a generator object
# print(big_list)


""" *
    *   
    *
    * """
# def my_range(n: int):
#     print("my_range starts")
#     start = 0
#     while start < n:
#         print("my_range is returning {}".format(start))
#         yield start
#         start += 1
#
#
# """ note that this example also explains why is it a bad idea to assign a generator to a variable """
# big_range = my_range(5)  # at this point nothing is executed, so use my_range directly in for loop
#
# print(next(big_range))  # the code is being executed here which yields the first value.
# print("big_range is {} bytes".format(sys.getsizeof(big_range)))
#
# # create a list containing all the values in big_range
# big_list = []
#
# for val in big_range:  # here the for loop is calling the next to get us the next value.
#     big_list.append(val)
#
# print("big_list is {} bytes".format(sys.getsizeof(big_list)))
#
# print(big_range)  # it will that it is a generator object
# print(big_list)
#
# """ *
#     *   so storing the my_range in big_range is fine if you want to call next each time you eant a new value
#     *   but it isn't a good idea if you intend using it again in a for loop
#     *   so replacing the big_range with my_range
#     * """
# print("looping again or not")
# for i in my_range(5):  # <-- replaced the big_range with my_range()
#     print("i is {0}".format(i))


""" *
    *   the range class behaves like interval in other words it reset's each time when it is used, which was not the case 
    *   when you used a variable that actually called the function
    *
    *   the range class behaves like an iterable, each time it is called it reset's.
    * """
def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


""" note that this example also explains why is it a bad idea to assign a generator to a variable """
big_range = range(5)  # <-- we are using the range method here

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []

for val in big_range:  # here the for loop is calling the next to get us the next value.
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))

print(big_range)  # it will that it is a generator object
print(big_list)

""" *
    *   so storing the my_range in big_range is fine if you want to call next each time you eant a new value 
    *   but it isn't a good idea if you intend using it again in a for loop
    *   so replacing the big_range with my_range
    * """
print("looping again or not")
for i in my_range(5):  # <-- replaced the big_range with my_range()
    print("i is {0}".format(i))