# ===================================
# writing to text file
# file=city_file: = is not assignment operator but it's a named argument
# ===================================

# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", "w") as city_file:
#     for city in cities:
#         print(city, file=city_file)  # here file= is mentioned, because we want to write content to file.

# ===================================
# trying to read the data written to file by above code
# ===================================
with open("cities.txt", "r") as city_file:
    for city in city_file:
        print(city)

# another way of removing(stripping)the newline character other than end=''
# strip will remove the matching char/string, starting from the beginning of
# the string or from the end of string

with open("cities.txt", "r") as city_file:
    for city in city_file:
        print(city.strip('\n'))

# ********Demo of strip*************
print()
sTest = "shreyas"
# it will do nothing as it was not able to find 'a' at the beginning or end of string
print(sTest.strip('a'))
# in this case it will remove /strip 's' from the beginning as well end of string,
# if anything in between i present than it is ignored.
print(sTest.strip('s'))


# ===================================
# sometimes the data written to file is not possible to read it back in original form
# ===================================
imelda = "More Mayhem", "Imelda MAy", "2011", (
    (1, "Pulling the Rug"), (2, "Pyscho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

with open("imelda3.txt", "w") as imelda_file:
    print(imelda, file = imelda_file)

# **********Output***************
# ('More Mayhem', 'Imelda MAy', '2011',
# ((1, 'Pulling the Rug'), (2, 'Pyscho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')))
# so it not possible to store it back into tuple as it is in string format.
# eval function does that, which evaluates the string to store the data back in tuple.
# eval is not good idea to use outside your data(data which is known to us).
with open("imelda3.txt", "r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)
print(imelda)
title, artist, year, tracks = imelda
print("Title: ", title)
print("Artist: ", artist)
print("Year: ", year)
print("Tracks: ", tracks)
