""" **************************************************************
    Strings in Python
****************************************************************** """

""" *
    *   Triple Quotes
    *
    *   you can define the string with the triple quotes
    *
    *   if you are using the double quotes or single quotes inside the triple quotes then there is no
    *   need of the escape sequence
    *
    *   when you split the string over multiple lines, each string is printed on the new line.
    * """

anotherString = """This string has been 
split over 
several
lines"""

print(anotherString)

print('*' * 20)

""" *
    *   so to avoid the printing of split string on new line, you can use backslash after every split string
    *
    *   using backslash will not split the string in the output.
    *
    *   Note that after backslash there shouldn't be any blank space
    * """
anotherString = """This string has been \
split over \
several \
lines"""
print(anotherString)

print()
print('*' * 50)
print()

""" *
    *   when you type a string with the escape character you need to be careful
    * """
# \t will be considered as the tab
# \n will be considered as the new line character
# print("C:\Users\timbuchalka\notes.txt")  # <-- this will result into error as \U is used for different purpose.

# to overcome this you can use either of the following
print("C:\\Users\\timbuchalka\\notes.txt")  # <-- you can use the double backslash

# OR

# you can use raw string, they are intended for use with regular expressions
print(r"C:\Users\timbuchalka\notes.txt")

print()
print('*' * 50)
print()

