# tuples are ordered set of data
# They ae similar to list.
# Tuples are immutable, that means they can't be changed
# a comma is used to separate the elements of a tuple, but the parentheses are only required when essential
# to remove syntactic ambiguity
# tuples

# t = 'a', 'b', 'c'
# print(t)

# this is not tuple and to remove the syntactic ambiguity we should add one more parentheses inside print
# the second one is what we need to make it tuple
# so when you are passing the tuple to function it needs to be in parentheses
# print('a', 'b', 'c')
# print(('a', 'b', 'c'))


# Creating Tuples
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", " Bad Company", 1974
# budgie = "Night flight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lighting", "Metallica", 1984

# print(metallica)

# we can also fetch the values from each index
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# as mentioned earlier tuples are immutable, they cannot be changed.
# for below initialisation it will give an error
# TypeError: 'tuple' object does not support item assignment
# uncomment below line  and run to check the error.
# metallica[0] = "Master of puppets"


# tuples support indexing and slicing
# which is sneaky way of actually correcting any problems or updating particluar entries
# so immutable doesn't mean that variable can't be assigned a new object of that type
# for e.g. in imelda variable, in 2nd value the spelling of imelda needs to be corrected
# imelda = "More Mayhem", "Emilda May", 2011 --> correction of Emilda to Imelda
# here the right hand side of expression is evaluated first
# print("Tuple Before Correction: ", imelda)
# imelda = imelda[0], "Imelda May", imelda[2]
# print("Tuple After Correction: ", imelda)

# to confirm the difference between
# mutable --> meaning it can be changed e.g. list
# immutable --> meaning it cannot be changed e.g. tuple
# 1. Mutable Object
# metallica2 = ["Ride the Lighting", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of puppets"
# print(metallica2)

# 2. Immutable Object
# Refer the previous example of imelda
# but we can assign the new object of that type


# unpacking the tuple values
# title, artist, year = imelda
# print("Title: ", format(title))
# print("Artist: ", format(artist))
# print("Year: ", format(year))

# We have added one more item to list.
# but we cannot be sure on how many items the list will contain while unpacking
## sumCount = metallica2.__len__()
# metallica2.append("Rock")
# title, artist, year = metallica2
# print("Title: ", format(title))
# print("Artist: ", format(artist))
# print("Year: ", format(year))

# Now we will try to append an item to tuple.
# AttributeError: 'tuple' object has no attribute 'append'
# uncomment the below line to execute it
# imelda.append("Jazz")

# tuple can contain an element that are themselves tuples.
# imelda = "More Mayhem", "Emilda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

# print(imelda)
# here we are assigning the tuple element to track
# title, artist, year, track = imelda
# print("Title: ", format(title))
# print("Artist: ", format(artist))
# print("Year: ", format(year))
# print("Track: ", format(track))

# in this case you got single tuple
# imelda = "More Mayhem", "Emilda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
#
# print(imelda)
# title, artist, year, track1, track2, track3, track4 = imelda
# print("Title: ", format(title))
# print("Artist: ", format(artist))
# print("Year: ", format(year))
# print("Track1: ", format(track1))
# print("Track2: ", format(track2))
# print("Track3: ", format(track3))
# print("Track4: ", format(track4))

# tuples containing the list
# tuples is immutable - we cannot change the tuples, but we can change the objects for same tuple
# list is mutable - which means we can change the content
imelda = "More Mayhem", "Emilda May", 2011, ([(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

imelda[3].append((5, "All For You"))
title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print("Title: ".format(title))
print("Artist: ".format(artist))
print("Year: ".format(year))
print("Tracks: ")
for song in tracks:
    track_no, track_name = song
    print("Track NO : {0} \t Track Name: {1}".format(track_no, track_name))


