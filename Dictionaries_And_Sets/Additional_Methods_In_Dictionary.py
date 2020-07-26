fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage" : "every child's favourite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)

# =================================
# Combining the 2 dictionaries
# dictionary does not return anything
# 1st example is adding fruit dictionary to veg
# 2nd example is  adding veg dictionary to fruit
# =================================
# veg.update(fruit)
# print("fruit dictionary added to veg dictionary: \n {}".format(veg))
#
# fruit.update(veg)
# print("veg dictionary added to fruit dictionary: \n {}".format(fruit))


# ====================================
# Create a new dictionary by combining both fruit and veg dictionary
# without changing the original dictionary
# use copy command and then update command
# ====================================

nice_and_nasty=fruit.copy()
nice_and_nasty.update(veg)
print("Nice And Nasty Dictionary: \n {}".format(nice_and_nasty))