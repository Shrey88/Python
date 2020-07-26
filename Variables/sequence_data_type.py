# Sequence data type
parrot = "Norwegian Blue"
print("Sequence data : " + parrot)
print()

# Printing single character from the sequence data
print("Printing single character from sequence data \"" + parrot + "\"" +" : " + parrot[3])
print()

# Printing single character in reverse order
print("Printing single character in reverse order : " + parrot[-2])
print()

# Printing sequence of character from sequence of data
print("Printing sequence of character from sequence of data : " + parrot[0:6])
print()

# Printing sequence of character from sequence of data in reverse order
# mentioning -1 as second index will skip the last character of sequence data
# mentioning [negative index : no index] will consider the last character of sequence data in reverse order
print("Printing sequence of character from sequence of data in reverse order : " + parrot[-5:])
print()

# Printing sequence of character from sequence of data
# mentioning only [No index:Index Number] end of index will start printing from starting position of sequence data
# i.e 0th index till the no of characters mentioned after colon
print("Mentioning only end of index without providing starting index : " + parrot[:6])
print()

# Printing sequence of character from sequence of data
# mentioning only [Index Number:No Index] start of index will start printing from mention position of sequence data
# till the end of sequence data.
print("Mentioning only start of index without providing end of index : " + parrot[6:])
print()

# Printing step characters
# [0:6:2] it will start printing the character from 0th position skipping 2 characters at a time
# but actually printing the 2nd character till the given end of index
print("Printing step characters : " + parrot[0:6:2])
print()

# Printing step characters
# [0::2] it will start printing the character from 0th position skipping 2 characters at a time
# but actually printing the 2nd character till the end of characters in sequence of data
print("Printing step characters till the end of characters: " + parrot[0::2])
print()

# Printing step characters
number = "9,223,372,036,854,775,807"
print("Step character example 1 : " + number[1::4])
print()

# Printing step characters
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print("Step character example 2: " + numbers[::3])
print()

# Printing the string multiple times
print("Printing the string multiple times : ")
print("Hello " * 5)
print()

# Substring check
print("Substring check")
today = "Sunday"
print("is word \"day\" substring of word " + today  + " : " )
print("day" in today)
print("is word \"Sun\" substring of word " + today  + " : " )
print("Sun" in today)
print("is word \"Thur\" substring of word " + today  + " : " )
print("Thur" in today)
print("is word \"parrot\" substring of word \"fjord\" : " )
print("parrot" in "fjord")
