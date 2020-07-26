# ================================
# shelve module provides shelf, you can think of it as dictionary
# but it is actually stored on file, rather in-memory.
# it holds key-value pair.
# value can be anything like pickled
# keys must be string unlike dictionaries where keys can be immutable objects such as tuple.
# all the methods used with dictionaries can be used with shelve objects.
# shelve always work in read-write mode so need to explicitly mention the mode of file
# the file created is or may be created with a DB extension automatically.
# Python actually uses database to store the data and pickles the values so that the complex
# python structure can be stored as database fields.
# we can use shelve similar to dictionary where we can assign the value to key and can
# access individual values using the keys
# shelves are persistent files
# ================================

import shelve

with shelve.open("shelfTest") as fruit:
    fruit["orange"] = "a sweet, orange, citrus fruit"
    fruit["apple"] = "good for making cider"
    fruit["lemon"] = "a sour, yellow citrus fruit"
    fruit["grape"] = "a small, sweet fruit growing in bunches"
    fruit["lime"] = "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])

print(fruit)
# *****Output******
# <shelve.DbfilenameShelf object at 0x002E9370>
# which says it shelve


# *********** 2nd Way of declaring shelve ********************
# in this case we need to explicitly specify the shelve.close()
# *************************************************************
# fruit = shelve.open("ShelfTest2")
# fruit["orange"] = "a sweet, orange, citrus fruit"
# fruit["apple"] = "good for making cider"
# fruit["lemon"] = "a sour, yellow citrus fruit"
# fruit["grape"] = "a small, sweet fruit growing in bunches"
# fruit["lime"] = "a sour, green citrus fruit"
#
# print(fruit["lemon"])
# print(fruit["grape"])
# fruit.close()
#
# print(fruit)


# ================================
# one difference to keep in mind between the shelve
# and a dictionary is that there's no shelve literal
# you can't initialise a shelve using a literal as we could with a dictionary.
# the below declaration is like dictionary which shelve does not support.
# so even though the shelve gets closed once its block is completed
# you are able to print : print(fruit["lemon"]) print(fruit["grape"] print(fruit)
# you wont find the same case with shelve(above code).
# ===============================
# with shelve.open("shelfTest") as fruit:
#     fruit = {"orange": "a sweet, orange, citrus fruit",
#              "apple": "good for making cider",
#              "lemon": "a sour, yellow citrus fruit",
#              "grape": "a small, sweet fruit growing in bunches",
#              "lime": "a sour, green citrus fruit"}
#
# print(fruit["lemon"])
# print(fruit["grape"])
# print(fruit)

# ===============================
# like dictionary we can print out key in shelve as well.
# ===============================
# for key in fruit:
#     print(key)

# ===============================
# deleting key's
# ===============================
# del fruit["lemon"]
# for key in fruit:
#     print(key)
# fruit.close()