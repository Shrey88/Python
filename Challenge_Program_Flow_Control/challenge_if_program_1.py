# Write a small program to ask for a name and age
# when both values have been entered, check if person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("Enter your name : ")
age = int(input("Enter your age : "))

if 18 < age < 31:
    print("Welcome to the holiday.")
else:
    print("Sorry, your age does not meet our criteria")
