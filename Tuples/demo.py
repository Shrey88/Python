# in this case, all four variables will be assigned the same value
a = b = c = d = 12
print("a: ", format(a))
print("b: ", format(b))
print("c: ", format(c))
print("d: ", format(d))

# another example will be A and B equals 12,13
# this is like unpacking the tuple(right hand side is same as how you define the tuple)
a, b = 12, 13
print("a: ", format(a))
print("b: ", format(b))

# we can also do something like this
# this is like unpacking the tuple(right hand side is same as how you define the tuple)
a, b = b, a
print("a: ", format(a))
print("b: ", format(b))
