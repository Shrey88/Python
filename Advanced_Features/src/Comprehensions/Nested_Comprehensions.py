""" ***************************************
    Nested Comprehension
******************************************* """
burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

# normal way of nesting the for loop
meal_list = []
for burger in burgers:
    for topping in toppings:
        meal_list.append((burger, topping))
print(meal_list)

""" *
    *   this is not a nested comprehension, it's actually 2 iterator parts.
    *   Python docs don't use the term nested comprehension, but you'll see people referring both 
    *   of our comprehension forms as nested comprehensions
    * """
meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

# the outer comprehension iterates over each item in toppings, then evaluates the expression for each one.
# the expression is itself a comprehension, that iterates over each of the burgers.
# when written like this, using another comprehension as the expression, the outer iteration values are used first.
for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)