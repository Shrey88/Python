# ======================================
# to check the built-in modules
# any module/method/function name starting with the double underscore should not be modified
# ======================================
print(dir())

# =====================================
# to check what the module contains
# =====================================

# print(dir(__builtins__))

# you can also use for loop to print
for m in dir(__builtins__):
    print(m)


# ====================================
# help command
# ====================================
import shelve
help(shelve)
