# =========================================================
# You can modify the value of key.
# keys are unsorted and the actual order is undefined for dictionary
# now the same is true for a shelve
# the good thing is if we iterate through the keys of our fruit and print them may be in alphabetical order
# shelve key must be a string and dictionaries themselves can accept any immutable object as a key
# shelve is not suitable for some applications, because the values are pickled before being stored
# and are unpickle by the value when it went
# considering that values are really complex this pickling and unpickling may impose significant overhead
# and affect the performance
# =========================================================
import shelve

with shelve.open('ShelfTest1') as fruit:
    fruit["orange"] = "a sweet, orange, citrus fruit"
    fruit["apple"] = "good for making cider"
    fruit["lemon"] = "a sour, yellow citrus fruit"
    fruit["grape"] = "a small, sweet fruit growing in bunches"
    fruit["lime"] = "a sour, green citrus fruit"

    # print(fruit["lemon"])
    # print(fruit["grape"])

    # before modifying the key, the value of lime
    # for snack in fruit:
    #     print(snack + " : " + fruit[snack])
    # print()

    # assigning the new value to the key
    # fruit["lime"] = " great with tequila"
    # print()

    # after modifying the key, the value of lime
    # for snack in fruit:
    #     print(snack + " : " + fruit[snack])

    # iterating through the while loop by entering the fruit key and displaying the value for it
    # while True:
    #     dict_key = input("Please enter a fruit: ")
    #     if dict_key == "quit":
    #         break
    #     if dict_key in fruit:
    #         description = fruit.get(dict_key)
    #         print(description)
    #     else:
    #         print("We don't have a " + dict_key)

    # for loop to print the keys in alphabetical order.
    ordered_keys = list(fruit.keys())
    ordered_keys.sort()

    for f in ordered_keys:
        print(f + "-" + fruit[f])
    print()

    # printing the values from shelve
    for v in fruit.values():
        print(v)
    print(fruit.values())  # values view object is printed, it cannot be modified

    print()

    for f in fruit.items():
        print(f)
    print(fruit.items())  # items view object is printed.
