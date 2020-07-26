# Dictionaries are unordered collections
# it guarantees that it will not have duplicates in collection
# Dictionaries ae key-value pair

# ======================================
# Fruit Example
# ======================================

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# fruit = {"orange": "a sweet, orange, citrus fruit",
#         "apple": "good for making cider",
#         "lemon": "a sour, yellow citrus fruit",
#         "grape": "a small, sweet fruit growing in bunches",
#         "lime": "a sour, green citrus fruit",
#         "apple": "round and crunchy"}  # previous value of apple will be replaced with this one

# displays the complete dictionary
# print(fruit)

# to print the the value for key in dictionary
# when you type-in the the first character of the key, IntelliSense shows you the complete name of the key.
# print(fruit["lemon"])

# Adding new entry to Dictionary
# fruit["pear"] = "an odd shaped apple"
# print(fruit)

# Assigning new value to existing key
# fruit["lime"] = "great with tequila"
# print(fruit)

# To remove any entry from dictionary
# del fruit["lemon"]
# print(fruit)

# To completely delete the dictionary
# you will get error that fruit is not defined
# del fruit
# print(fruit)

#  To clear dictionary
# fruit.clear()
# print(fruit)

# Key does not exist in dictionary
# it will give key error
# print(fruit["tomato"])

# Accessing the values of key entered by user.
# while True:
#     dict_key = input("Enter a Fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have key " + dict_key)

# Alternative way of printing the else print statement
# while True:
#     dict_key = input("Enter a Fruit : ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key,"We don't have key " + dict_key)
#     print(description)

# To print all the values for the key present in dictionary
# for snack in fruit:
#     print(fruit[snack])

# To print the dictionary in ordered format
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# Alternative to sorting list and assigning it to variable in single statement
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + ' - ' + fruit[f])

# instead of assigning the sorted keys to variable we can use directly in for loop
# for f in sorted(fruit.keys()):
#     print(f + ' - ' + fruit[f])

# 1st View Object
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = " not nice with ice cream"
# print(fruit_keys)

# 2nd view object is items object
# it returns the list of tuples.
# print(fruit.items())

# we can also produce tuples from this using tuple function
# f_tuples = tuple(fruit.items())
# print(f_tuples)

# way to create dictionary from tuple
# print(dict(f_tuples))

# creating a single string out of this list
my_List = ["a", "b", "c", "d"]
new_string = ""
for c in my_List:
    new_string += c + ","  # this is creating new copy of variable new_string every time for loop is executed
print(new_string)

# this also solves the problem of trailing comma as we have seen in previous for loop output
new_string = ",".join(my_List)
print(new_string)

# new string created from existing string with comma separated
letters = "abcdefghijklmnopqrstuvwxyz"
new_string = ",".join(letters)
print(new_string)

# ======================================
# Motorbike Example
# ======================================
# bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine-size":250}
# print(bike)
# print(bike["engine-size"])
# print(bike["colour"])
