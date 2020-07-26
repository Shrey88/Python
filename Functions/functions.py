# ===========================================================================================
# in python functions are created with the word "def" followed by the function name and
# a pair of parenthesis and semi-colon
# parameters refer to the variables defined in the function
# arguments refer to the actual values used when the function is called.
# ===========================================================================================


# def python_food():
#     print("spam and eggs")


# call the function
# python_food()

# if you do not define the return statement in the function and you call that function, it will return "None"
# print(python_food())


# def centered_text(text):
#     text = str(text)
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text)


# calling the function
# centered_text("Spam and Eggs")
# centered_text("Spam, Spam and Eggs")

# this will not work as number does not have len which we are calculating in the function
# so to convert the input argument to string we are going to use "str" in the function
# centered_text(12)
# centered_text("Spam, Spam, Spam and Eggs")


# ============================================
# multiple arguments to a function
#
# ============================================

#
# def multiple_arg(*args):
#     text = ""
#     for arg in args:
#         text += str(arg) + " "
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text)


# calling the function taking multiple arguments
# multiple_arg("first", "second", 3, 4, "spam")


# ============================================
# creating user defined function which behave same as the print function
#
# ============================================


# def custom_print(*args, sep=' ', end='\n', file=None, flush=False):
#     text = ""
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text, sep=sep, end=end, file=None, flush=flush)
#
#
# # calling the function custom_print
# custom_print("first", "second", 3, 4, "spam")
# custom_print("first", "second", 3, 4, "spam", sep=':')


# ===========================================
# writing to a file using print function itself
#
# ===========================================
# def custom_print(*args, sep=' ', end='\n', file=None, flush=False):
#     text = ""
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text, sep=sep, end=end, file=file, flush=flush)
#
#
# with open("custom_print_file", mode="w") as custom_print_file:
#     # calling the function custom_print
#     custom_print("first", "second", 3, 4, "spam", file=custom_print_file)
#     custom_print("first", "second", 3, 4, "spam", sep=':', file=custom_print_file)
#     custom_print("Spam and Eggs", file=custom_print_file)
#     custom_print("Spam, Spam and Eggs", file=custom_print_file)
#     custom_print(12, file=custom_print_file)
#     custom_print("Spam, Spam, Spam and Eggs", file=custom_print_file)


# ==============================================
# we will return the string from the function back
# and print it on screen
# ==============================================
def custom_print(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# calling the function custom_print
print(custom_print("first", "second", 3, 4, "spam"))
print(custom_print("first", "second", 3, 4, "spam", sep=':'))
print(custom_print("Spam and Eggs"))
print(custom_print("Spam, Spam and Eggs"))
print(custom_print(12))
print(custom_print("Spam, Spam, Spam and Eggs"))
