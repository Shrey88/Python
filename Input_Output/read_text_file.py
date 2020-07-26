# ==================================
# Reading the content of file
# ==================================

# provide the path if file is not present at the location where code is available
# readFile = open("D:\\Python\\Input_Output\\sample.txt", "r")

# readFile = open("sample.txt", "r")
#
# for line in readFile:
#     print(line, end="\n")  # you can convert the words in line to lower cases i.e line.lower()
#
# readFile.close()


# ==================================
# with statement
# it will tidy everything up automatically once the object's no longer needed.
# there is no need to explicitly close the file.
# if there is error while reading the file,
# with will take care of closing the file before the programs terminates
# ==================================
# with open("sample.txt","r") as readFile:
#     for line in readFile:
#         if "JAB" in line.upper():
#             print(line, end='')

# ==================================
# readlines : it reads the complete file into memory
# converts the line into list format
# ==================================
# with open("sample.txt","r") as readFile:
#     lines = readFile.readlines()
# print(lines)

# to print each element of list
# for line in lines:
#     print(line, end='')

# ======================================================================
# readlines and slicing with -1: it reads the complete file into memory
# converts the line into list format and
# the foreach is reading the lines in reverse order
#
# read and slicing with -1 :it reads the complete file
# it does not store the data ito memory like readlines
# it can optional parameter specifying the amount data to be read.
# the foreach is reading the lines not only in reverse order,
# but also reversing the words
# ======================================================================
with open("sample.txt","r") as readFile:
    lines = readFile.readlines()

print(lines, end='')

for line in lines[::-1]:
    print(line,end='')

print()
print()

with open("sample.txt","r") as readFile:
    lines = readFile.read()

print(lines,end='')

for line in lines[::-1]:
    print(line, end='')