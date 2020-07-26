# for loop
# for i in range (1, 12):
#     print("No {} squared is {} and cubed is {:4}".format(i, i**2, i**4) )

# printing individual character
# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     print(number[i])

# Skipping the separator and printing the rest of the characters
number = "9,223,372,036,854,775,807"
cleanedNumber = ''
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
#
# # you can overwrite the default behavior of printing the characters on new line
# # by changing argument of end in print with end=''
# newNumber = int(cleanedNumber)
# print("The New Number is {}".format(newNumber), end='')

# instead of using len(number) for calculating the length of string
# we can write in following way
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)
# print("New Number is {}".format(newNumber))

# for loop with list
# for state in ["not pinin", "no more", "a stiff", "bereft of life"]:
#     print("This Parrot is {}".format(state))

# for loop with step value
# for i in range(0, 100, 5):
#     print("i is {}".format(i))

# Tables
# for i in range (1, 21):
#     for j in range (1, 21):
#         print("{1} times {0} is {2}".format(j, i, i*j))
#     print("========================")

# other way to print tables
# for i in range (1, 21):
#     for j in range (1, 21):
#         print("{1} times {0} is {2}".format(j, i, i*j), end='\t')
#     print('')

#indenting the output
for i in range(2,13):
    for j in range(1,13):
        print("{1:>2} times {0} is {2}".format(i, j, i*j)) #

    print('-' * 15)