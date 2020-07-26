# different ways of defining the list
# one using the square brackets "[" / "]"
# other one is calling the list constructor
List_1 = []
List_2 = list()

print("List 1 : {}".format(List_1))
print("List 2 : {}".format(List_2))

# if you compare both the list they will result to true, as both list are empty list
# created by 2 different ways.
# if List_1 == List_2:
#     print("Lists are equal")
# else:
#     print("Lists are not equal")

# list are iterable.
# print(list("The lists are equal"))

# list can be named reference to another variable.
# so here in this case we are referencing even variable to another_even variable.
# whatever changes made to another_even will also affect the even variable.
even = [2, 4, 6, 8]
# here assignment operator "=" works as reference.
another_even = even

# "is" operator is object identity check operator.
# its checks if both the objects are pointing to same memory location
# or both are same object
print("Both the variables are same : ", another_even is even)

another_even.sort(reverse = True)
print(even)
