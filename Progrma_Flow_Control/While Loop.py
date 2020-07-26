""" =============================================================================
    while loop :
================================================================================= """

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

""" ============================================================================== 
================================================================================== """
# available_exits = ["east", "north east", "south"]
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction : ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
#     else:
#         print("aren't you glad you got out of there")

""" ==============================================================================
    Guess Game
================================================================================== """
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")

""" =============================================================================
    while....else loop :    when there is no break or return statement then 
                            the else condition is executed
================================================================================= """