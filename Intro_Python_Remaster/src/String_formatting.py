"""
    String Formatting
"""

""" *
    *   setting the field width the value mentioned after the colon is for setting the width
    *
    *   you can use the <(left align) / >(right align) / ^(center align) symbols along with the width value
    *   i.e. :<4 / :>4 / :^4
    * """
for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))

print()

""" *
    *   for floating point values we can specify the precision (the number of digits after the decimal point)
    *
    *   so the value after the colon contains the width as well as the number of digits to print after decimal point
    * """
print("Pi is approximately {0:12}".format(22 / 7))  # <-- defaults to printing 15 decimals
print("Pi is approximately {0:12f}".format(22 / 7))  # <-- we  get default of 6 digits after the decimal point
print("Pi is approximately {0:12.50f}".format(22 / 7))  # <-- python decides that precision is more important than field width, so ignoring specified width
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))


""" *
    *   string interpolation
    *
    *   here the %d will be replaced by an integer value that's provided after the string
    *   following another % character
    *
    *   to inject the float value you need to mention %f in place of %d or %s for string
    * """
age = 25
print("My age is %d years" % age)

letters = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(letters[:-1:5])