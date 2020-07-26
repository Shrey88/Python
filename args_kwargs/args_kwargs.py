import builtins
""" ===================================================================
    so if you click on the print method you will see that the first argument
    is *args which allows the print method to take number of arguments
    so our three strings are wrapped up in a tuple

    so args or *args is the unpacked values in that tuple.
    Args itself is a tuple, and the print function takes each from the tuple
    and then prints it.
======================================================================= """
# print("Hello", "World", "earth")


""" ======================================================================================
    the below code shows how the *args are iterated.
    this is variadic parameter and it must appear after all other positional parameters.
    
    So basically you can't do something like this 
        def average (first_value, *args, last_value) <-- wrong way of declaring 
        def average (first_value, last_value, *args) <-- right way of declaring
    
    So if anything follows the *args, then it has to be a set of keyword parameters
========================================================================================== """
# def average(*args):  # <-- *args represents the unpacked tuple
#     print(type(args))
#     print("args is {}".format(args))  # <-- args without star is a tuple
#     print("*args is:",*args)  # <-- this has unpacked the args tuple on line four
#     mean = 0
#     for arg in args:
#         mean += arg
#     return mean/len(args)
#
#
# print(average(1, 2, 3, 4))


""" =========================================================================================
    it works the same way as packing a variable number of elements of arguments into a tuple
    but this time we need to pack a variable number of named arguments, or keyword arguments
    
    **kwargs unpacks the dictionary in same way like tuple.
    
============================================================================================= """
# def print_backwards(*args, **kwargs):
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)
#
# with open("backwards.txt", "w") as backwards:
#     print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards)

""" =========================================================================================================
    Problem:    there is now problem here, the print_backwards calling function end='\n'
                then you will get the TypeError saying that print function has got multiple values for 
                the keyword argument 'end'
============================================================================================================= """
# def print_backwards(*args, **kwargs):
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)
#
# with open("backwards.txt", "w") as backwards:
#     print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards, end='\n')

""" ===========================================================================================
    Solution 1 :    add the end keyword to the function definition
                    
    there is a slight difference though *args deals with positional arguments. If they don't have names
    they should just appear in order in the function call
    
    but **kwargs uses the parameter/argument names, so it doesn't care what order we specify them in when calling
    the function, it just scoop's up that our function hasn't been declared and puts them on kwargs.
                    
=============================================================================================== """
# def print_backwards(*args, end = ' ', **kwargs):
#     for word in args[::-1]:
#         print(word[::-1], end=end, **kwargs)
#
# with open("backwards.txt", "w") as backwards:
#     print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader")
#     # print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards, end='\n')

""" ===========================================================================================
    Solution 2 :    
=============================================================================================== """
# def print_backwards(*args, **kwargs):
#     end = kwargs.pop('end', None)
#     for word in args[::-1]:
#         print(word[::-1], end=end, **kwargs)
#
#
# with open("backwards.txt", "w") as backwards:
#     print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards)

""" ============================================================================================
    Solution 3:
================================================================================================ """
# def print_backwards(*args, **kwargs):
#     end_character = kwargs.pop('end', '\n')
#     separator_character = kwargs.pop('sep', ' ')
#     for word in args[::-1]:
#         print(word[::-1], end=separator_character, **kwargs)
#     print(end=end_character)  # <-- by default the end character is newline character, but since we have changed the end character in the above line we need to explicitly assign it.
#
#
# with open("backwards.txt", "w")as backwards:
#     print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
#     print("Another String")
#
#
# print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')

""" =============================================================================================
    Solution 4:
================================================================================================= """
# def print_backwards(*args, **kwargs):
#     end_char = kwargs.pop('end', '\n')  # <-- fetching the value of end from kwargs
#     sep_char = kwargs.pop('sep', ' ')  # <-- fetching the value of sep from kwargs
#     for word in args[:0:-1]:
#         print(word[::-1], end=sep_char)
#     print(args[0][::-1], end=end_char)  # <-- print the first word separately
#
#
# print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')

""" =============================================================================================
    Solution 5:
================================================================================================= """
def backwards_print(*args, **kwargs):
    sep_char = kwargs.pop('sep', ' ')
    print(sep_char.join(word[::-1] for word in args[::-1]), **kwargs)


backwards_print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')