# # it tells us that range value starts from 0 and ends at 99
# # print(range(100))
# #
# # # list is created with values from 0 to 9
# # my_list = list(range(10))
# # print(my_list)
# #
# # # creating list of even digits starting from 0 and skipping 2 values
# # even = list(range(0, 10, 2))
# # print(even)
# #
# # # creating list of even digits starting from 0 and skipping 2 values
# # odd = list(range(1, 10, 2))
# # print(odd)

# getting the index of char or char at index in string
# my_string = "abcdefghijklmnopqrstuvwxyz"
#
# # finding the index no for 'e'
# print(my_string.index('e'))
#
# # finding the char at index no 4
# print(my_string[4])
#
# # this will tell you the range assigned to variable
# small_decimals = range(0, 100)
# print(small_decimals)
#
# # we can use index for range as well
# print(small_decimals.index(3))
#
# odd = range(1, 10000, 2)
# print(odd)
#
# # it prints the value at the index 985
# print(odd[985])
#
# # We can also check if the inut value provided is the range or not
# sevens = range(7, 1000000, 7)
# x = int(input("Please enter a positive number less than a million: "))
# if x in sevens:
#     print("{} is divisible by seven".format(x))
# else:
#     print("{} not divisible by 7".format(x))
#
# # slicing the defined range into range of even numbers
# # check the the range of small decimals
# print(small_decimals)
#
# creating slicing on the existing range by 2
# slicing meaning getting value from range present at every 2nd index.
# my_range = small_decimals[::2]
# print(my_range)
#
# # getting the index of value 4
# print(my_range.index(4))

#
decimals = range(0, 100)
print(decimals)

# here my_range is list containing the numbers starting from value 3 and ends before 40
# by slicing 3 values
my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print("=" * 40)

for i in range(3, 40, 3):
    print(i)

# you can check for equality
# my_range variable is defined as sequence of numbers starting from 3 and
# skipping next 3 numbers and ending at 40
# where as range(3, 40, 3) is doing the same.
print(my_range == range(3, 40, 3))

# In this example you will see that even if though the
# range ending value is different it returns true.
# because it checks for the sequence of values from both the range
print(range(0, 5, 2) == range(0, 6, 2))

# to verify why it is above case is returning true
# we will create 2 list using both the range and print the value from it
# you will find that the sequence of values inside 2 list are same and that
# is why equality check returns true.
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))


# another example of equality check returning true.
r = range(0, 100)
print(r)

for i in r[::-2]:
    print(i)

print("=" * 50)

for i in range(99, 0, -2):
    print(i)

print(r[::-2] == range(99, 0, -2))
# you can type r[::-2] in below format as well
print(range(0, 100)[::-2] == range(99, 0, -2))

# but whe you want to read the values using range(0, 100,-2)
# it will not return any thing because the start and end value should be reversed in this case.
for i in range(0, 100, -2):
    print(i)

# negative step is represented as (start Value, end Value, negative step)
# negative slice is represented as [start value:end value:negative slice]

# but range with negative step can be useful
backString = "eguagnal lufrewop yrev a si nohtyP"
print(backString[::-1])

r = range(0, 10)
for i in r[::-1]:
    print(i)
