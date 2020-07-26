""" *
    *   even though the variable is defined inside the if condition it is still accessible outside.
    *   blocks do not define scope in python
    * """

if (True):
    z = 112
    print('line 123')

print(z)