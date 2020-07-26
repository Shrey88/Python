# Printing the string along with number
# In python we need to explicitly convert number to str with use of str func

age = 24
print("Converting number to string format to be used with string")
print("My age is " + str(age) + " years")
print()

# Replacement field
print("Using single replacement field")
print("My age is {0} years".format(age))
print()

# Multiple Replacement field
print("Using multiple replacement field")
print("There are {0} days in months of {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Januray", "March", "May", "July", "August", "October", "December"))
print()

# Using Multiple replacement field with triple quote
print("Using multiple replacement field with triple quote")
print("""January : {2}
"February" : {0}
"March" : {1}
"April" : {2}
"May" : {1}
"June" : {2}
"July" : {1}
"August" : {1}
"September" : {2}
"October" : {1}
"November" : {2}
"December" : {1}
""".format(28,30,31))
print()

# Old format used in python 2
print("*****************************Old Format used in Python 2***********************************")
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))
print()

# integer precision with old format
print("Integer precision with old format")
for i in range (1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i,i**2,i**3))
print()

# float precision with old format
print("Float precision with old format")
print("(No Precision)Pi is approximately %f" % (22 / 7))
print("(Precision of 12)Pi is approximately %12f" % (22 / 7))
print("(No Precision)Pi is approximately %12.50f" % (22 / 7))
print()

# Precision with Replacement field with new format
# second parameter in the replacement field is the precision no
print("******************Precision with Replacement field with new format******************************")
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))
print()

print("Aligning the numbers on left")
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))
print()

print("(No Precision)Pi is approximately {0:4}".format(22 / 7))
print("(Precision of 12)Pi is approximately {0:12}".format(22 / 7))
print("(No Precision)Pi is approximately {0:12.50}".format(22 / 7))