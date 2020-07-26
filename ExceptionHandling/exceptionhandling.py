"""
    so there are two types of error:
        1. syntax errors
        2. exception : we may get errors as a result of flaws in the code's logic or conditions that we couldn't predict
            for e.g. we are trying to create a database and there isn't enough space on the drive that we specify.
"""


""" =====================================Exception Handling===================================== """
import sys


# def factorial(n):
#     # n! can also be defined as n * (n-1)!
#     """ calculates n! recursively """
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# """ code inside the try block runs first and if any exception occurs then it jumps directly to except """
# try:
#     print(factorial(1000))
# except RecursionError:
#     print("This program calculate factorials that's large")
#
# print("Program Terminating")
""" ==============================================================================================="""

""" =================================Multiple Exception Handling================================"""


# def factorial(n):
#     # n! can also be defined as n * (n-1)!
#     """ calculates n! recursively """
#     if n <= 1:
#         return 1
#     else:
#         print(n/0)  # in this case the exception was not handle as we did not define the exception for ZeroDivisionError
#         return n * factorial(n-1)
#
#
# """ we are adding one more exception """
# try:
#     print(factorial(1000))
# except RecursionError:
#     print("This program calculate factorials that's large")
# except ZeroDivisionError:
#     print("Natural numbers cannot be divided by Zero")
# print("Program Terminating")
""" =============================================================================================== """

""" =================================Multiple Exception Handling================================= """


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(1)


first_number = getint("Please enter first number: ")
second_number = getint("Please enter second number: ")

try:
    print("{} is divided by {} is {}".format(first_number, second_number, first_number/second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)

print("Program Terminating")
""" ============================================================================================ """

""" ================================= Exception Handling With Exit Codes ================================= """


# def factorial(n):
#     # n! can also be defined as n * (n-1)!
#     """ calculates n! recursively """
#     if n <= 1:
#         return 1
#     else:
#         print(n/0)  # in this case the exception was not handle as we did not define the exception for ZeroDivisionError
#         return n * factorial(n-1)
#
#
# """ how to handle more than 1 exceptions """
# try:
#     print(factorial(1000))
# except (RecursionError, ZeroDivisionError):
#     print("This program calculate factorials that's large")
#
# print("Program Terminating")
""" ============================================================================================ """
