""" =================================================================================================================
    There are two optional cases in exception handling:
        1) else :   it must come after all the except clause and before finally clause.
                    it will be executed if the try block completes the execution of the code successfully.

        2) finally :    will always be executed regardless of whether an exception was handled or not, so in the
                        finally block, you would be doing things like closing a database cursor or connection
                        or closing any open file any those types of things.
==================================================================================================================="""
import sys


""" =================================Exception Handling using else/finally ================================= """


# def getint(prompt):
#     while True:
#         try:
#             number = int(input(prompt))
#             return number
#         except ValueError:
#             print("Invalid number entered, please try again")
#         except EOFError:
#             sys.exit(1)
#         # else:
#         #     print("getint :: In the else condition")
#         finally:
#             print("getint :: The final clause always executes")
#
#
# try:
#     first_number = getint("Please enter first number: ")
#     second_number = getint("Please enter second number: ")
#     print("{} is divided by {} is {}".format(first_number, second_number, first_number/second_number))
# except ZeroDivisionError:
#     print("You can't divide by zero")
#     sys.exit(2)
# else:
#     print("Division performed successfully")
# finally:
#     print("The main final clause always executes")
#
# print("Program Terminating")
""" ============================================================================================ """

""" =================================Exception Handling using else/finally ================================= """

"""
    so as per the documentation not all the exceptions have to e derived from exception.
    the requirement is that they are derived from the base exception or one of its subclasses so if you
    really want to catch any exception then there's a way to specify the sort of wild card exception meaning 
    everything to do that just leave off the exception type so the except clause is just the keyword
"""


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        except:
            print("Invalid number entered, please try again")
        finally:
            print("getint :: The final clause always executes")


try:
    first_number = getint("Please enter first number: ")
    second_number = getint("Please enter second number: ")
    print("{} is divided by {} is {}".format(first_number, second_number, first_number/second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("Division performed successfully")
finally:
    print("The main final clause always executes")

print("Program Terminating")
""" ============================================================================================ """
