# =========================================================
# =========================================================

import shelve

# with shelve.open("bike") as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engine_size"] = 250
#
#     print(bike["engine_size"])
#     print(bike["colour"])


# =========================================================
# unlike a dictionary examples where we could run the program
# again and every thing started from scratch.
# shelves are persisted in files
# we are adding engine size with the key name as engin_size
# we will try to access the engine size with key as engine_size
# =========================================================

# with shelve.open("bike2") as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engin_size"] = 250
#
#     print(bike["engine_size"])  # this will report an error.
#     print(bike["colour"])

with shelve.open("bike2") as bike:
    # bike["make"] = "Honda"  # commented out, so that we don't add it again to the file
    # bike["model"] = "250 dream"  # commented out, so that we don't add it again to the file
    # bike["colour"] = "red"  # commented out, so that we don't add it again to the file
    # bike["engine_size"] = 250  # corrected the key from engin_size to engine_size

    # just because it was a typo error doesn't mean that it will be removed from persistent file
    # so it still holds the value for key engin_size
    # print(bike["engin_size"])
    # print(bike["engine_size"])
    # print(bike["colour"])

    # just like dictionary we can iterate through the shelve
    # so when you print the keys you will find that engin_size key still exists.
    # for key in bike:
    #     print(key)

    # like dictionary you can delete the keys.
    # del bike["engin_size"]
    # # iterate trough the keys in bike and you will see that the key is removed
    for key in bike:
        print(key)



