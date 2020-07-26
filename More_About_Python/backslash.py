# backslash Character

# splitting a string into several lines
# with help of new line character
print("New Line Character : ")
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)
print()

# placing tab between characters
print("Tab : ")
tabbedString = "1\t2\t3\t4\t5\t"
print(tabbedString)
print()

# using same quote as starting and ending quote in string
print("using same quote as starting and ending quote in string : ")
print("1 : single quote inside single quote")
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting"')
print()
print("2: double quote inside double quote")
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\"")
print()

# to avoid using the new line character
print("Using triple quotes to split string :")
anotherSplitString = """This string has been
split over
several lines"""
print(anotherSplitString)
print()

# avoiding splitting of lines into multiple lines
print("Avoid splitting of lines into multiple lines : ")
anotherSplitString_1 = """This string has been \
split over \
several lines."""
print(anotherSplitString_1)
print()

