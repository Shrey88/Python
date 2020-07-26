""" =============================================================================
    if condition :
================================================================================= """

""" =============================================================================
    type conversion from string to int.
================================================================================= """
# name = input("Please enter your name : ")
# age = int(input("How old are you, {}? ".format(name)))
# print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box.")
# else:
#     print("Please come back in {0} years".format(18 - age))

""" =============================================================================
    Number Guess Program
================================================================================= """
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess != 5:
#     if guess < 5:
#         print("Please guess higher.")
#     else:
#         print("Please guess lower.")
#
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it right")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You guessed it in first chance")


""" =============================================================================
    Advance if, elif and else
================================================================================= """
# age = int(input("How old are you? "))

# if (age >= 16) and (age <= 65):
# similar condition can be written in below format
# if 15 < age < 66:
#     print("Have a good day at work")

# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

""" =============================================================================
    Python does not have boolean dataatype but it has function/method called bool
    which returns true or false value
================================================================================= """
# print(bool(age))


""" =============================================================================
    use of not
================================================================================= """
# if not(age < 18):
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))


""" =============================================================================
    finding character in variable and validating it
================================================================================= """
# parrot = "Norwegian Blue"
#
# letter = input("Enter a character : ")

# if letter in parrot:
#     print("Give me an {}, Bob".format(letter))
# else:
#     print("I don't find that letter")

""" =============================================================================
    reversing the condition and making use of not
================================================================================= """
# if letter not in parrot:
#     print("I don't find that letter")
# else:
#     print("Give me an {}, Bob".format(letter))

""" =============================================================================
list with continue command
================================================================================= """
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        print("Ignoring item : {}".format(item))
        continue
    print("Buy " + item)
