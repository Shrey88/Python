# create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.


inputString = input("Enter some characters: ")
vowels = frozenset("aeiou")

# mySet = set(inputString)
# finalSet = mySet.difference(vowels)

# finalSet can also be written as
finalSet = sorted(set(inputString).difference(vowels))

# finalSet = sorted(finalSet)
print(finalSet)
