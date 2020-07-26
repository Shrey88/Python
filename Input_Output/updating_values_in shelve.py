# =====================================================
# updating the values in shelve
# =====================================================

import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scramble_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "Cheese"]

with shelve.open("recipe", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scramble_eggs"] = scramble_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # adding new values to existing keys
    # so what actually happen is that we have appended items
    # to a copy of the list read into memory but haven't provided any trigger for the shelve
    # to write data back out again, the reason that it works this way is to keep
    # the disk access to an absolute minimum, so that values are not written continuously
    # but it does have this unfortunate side effect tha when accessing the same keys after a change causes it to
    # be read from the shelve and that's the unchanged value is returned

    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

    # so there are two methods
    # 1.
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # 2. you can directly update the shelve by setting writeback as true
    # when you actually use writeback Python caches the object in memory and doesn't actually update the
    # shelve file itself until you close the shelve or used a sync method
    # so if there's been a lot of changes closing a shelve can take a while
    # because all have to be written to disk at once so this gives the advantage.
    # recipes["soup"].append("croutons")

    # sync method works when the shelve file is closed
    # but to immediately sync the values soon after the value is appended
    # this method is not recommended to sync the value as soon as it is appended.
    # over writing the value for soup
    recipes["soup"] = soup
    recipes.sync()
    soup.append("cream")  # so the soup key will not have cream value in it as it is not written to disk

    print()

    for snack in recipes:
        print(snack, recipes[snack])