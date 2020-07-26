# 1st list
even = [2, 4, 6, 8]

# 2nd list
another_even = list(even)

# as you see both the list are independent
# they are pointing to 2 different memory location because.
# 1st list we have created with inputs in square braces
# 2nd list we have created with list constructor.

# in this case it will return false as the objects are pointing to different memory location.
print("is Operator : ", another_even is even)

# in this case it will return true as the "==" is checking for the contents
print("== Operator : ", another_even == even)


another_even = sorted(even, reverse = True)

# now after reversing the list and assigning it to variable another_even
# comparing the 2 different objects
# in both the case it will return false
# 1st because the contents are reversed.
# 2nd even though we have not used square brackets or list constructor to define 2nd list
# still sorted function assigns it list to another_even variable pointing to different memory location.

print("After reversing the list using \"==\" operator : ", another_even == even)
print("After reversing the list using \"is\" operator: ", another_even is even)
