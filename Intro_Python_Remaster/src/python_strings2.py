""" *********************************************************
    String Slicing
************************************************************* """

parrot = "Norwegian Blue"

""" *
    *   here we are slicing the string starting from the position 0 and stopping at 6
    *   i.e. we are going upto 6 but not including the 6th character(we are only including till the 5th character)
    *
    *
    *   even if you don't won't to provide either the start or stop value, you have to provide the : symbol so that
    *   python understands that you want to slice the string.
    * """
print(parrot[0:6])

# if you don't won't to provide the start value you can write
print(parrot[:6])

# printing the last 4 characters
print(parrot[10:14])

# if you don't won't to provide the stop value you can write
print(parrot[10:])


""" *
    *   using the negative number in slicing the string
    * """

# you can't go backwards from the starting position
print(parrot[-4:2])  # <-- it doesn't print anything
# if you want to print the strings backwards then slice it by -1
print(parrot[-4:2:-1])  # <-- this will print the characters from the start position to stop position by stepping -1 character


""" *
    *   Using Step value with slice value, the default slice value is one 
    * """
print(parrot[0:6:2])  # <-- stepping on the 2nd character from the current position
print(parrot[0:6:3])  # <-- stepping on the 3rd character from the current position


""" *
    *   Slicing Backwards
    * """
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)

""" *
    *   negative value counts from the end of the sequence, which means -1 is the last character in the string
    *   which means we have requested a slice that extends from the z up to, but not including the z and 
    *   therefore we get nothing.
    *
    *   the other obvious reason is to omit the stop value
    * """
backwards = letters[25:-1:-1]
print(backwards)

# python recognizes it as reversing the sequence
backwards = letters[25::-1]
print(backwards)

# ::-1 is a python idiom, python recognizes it as reversing the sequence
backwards = letters[::-1]
print(backwards)

# create a slice that produces the characters qpo
print(letters[-10:-13:-1])
print(letters[16:13:-1])

# slice the string to produce edcba
print(letters[-22::-1])
print(letters[4::-1])

# slice the string to produce the last 8 characters in reverse order
print(letters[-1:-9:-1])
print(letters[:-9:-1])