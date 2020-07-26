# Guess Game
import random

highest = 1000
answer = random.randint(1, highest)
iGuess = 0

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess != answer:
    while guess != answer:
        if iGuess == 10:
            print("Exceeded number of guesses")
            break

        if guess == 0:
            break
        elif guess < answer:
            print("Please guess higher. Enter 0 to quit")
            iGuess += 1
        elif guess > answer:
            print("Please guess lower. Enter 0 to quit")
            iGuess += 1
        elif guess == answer:
            print("Well done, you guessed it")
            break

        guess = int(input())
else:
    print("You got it first time")
