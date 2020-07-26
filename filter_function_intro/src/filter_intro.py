""" ****************************************************
    Filter Intro

    just like map filter takes two arguments:
        1: the function that does the filtering
        2: interval to iterate over.
******************************************************** """

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# normal way of iterating
for meal in menu:
    if "spam" not in meal:
        print(meal)

print()

# comprehension way of iterating
meals = [meal for meal in menu if "spam" not in meal]
print(meals)

print()

# filter function
""" *
    *   filter function does the same thing but it needs to create a function that only 
    *   returns true if an item is what we want.
    * """
def not_spam(meal_list: list):
    return "spam" not in meal_list

spamless_meals = list(filter(not_spam, menu))
print(spamless_meals)