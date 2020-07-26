""" *************************************************************
    List Comprehensions

    scope of the variable used in the for loop will be confined to comprehension only
***************************************************************** """

print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

""" *
    *   this is how you would iterate over the list normally and store the result back in the list format
    * """
squares = []
for number in numbers:
    squares.append(number ** 2)
# print(squares)


""" *
    *   this is how you would write the same code in comprehension format
    *   to store the result back into the list you will just put the square brackets around the expression.
    *   the list comprehension contains the two parts 
    *       the first one is expression that we want to return number to power 2 in this case
    *       the second part is an iteration over a sequence and we don't need the colon at the end.
    * """
squares1 = [number ** 2 for number in numbers]

# print(squares1)

""" *
    *   Conditional comprehension
    * """
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

""" *
    *   normal format of conditonal expression
    * """
# for meal in menu:
#     if "spam" not in meal:
        # print(meal)

""" *
    *   Comprehension format of conditional expression
    *   Now comprehension has 3 parts 
    *       the first is the expression
    *       the second is the iteration
    *       the third is the filter that can have one or more filters
    * """
meals = [meal for meal in menu if "spam" not in meal]
# print(meals)

""" *
    *   if you want to use two conditions in the comprehension 
    *   make use of "and" in between two conditions 
    * """
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
# print(meals)

""" *
    *   sometimes you want to meet some conditions that cannot be taken care in one filteration
    *   for e.g. customer does not want a meal that has bacon and sausage together.
    * """
fussy_meal = [meal for meal in menu if "spam" in meal or "eggs" in meal if not ("bacon" in meal and "sausage" in meal)]
# print(fussy_meal)

""" *
    *   the above comprehension can also be written in this form
    * """
fussy_meal = [meal for meal in menu if ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in meal)]
# print(fussy_meal)

""" *
    *   so we want to have else condition in comprehension incase the if confition is not met.
    * """
# normal way of doing it is
meals=[]
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)
#     else:
#         meals.append("a meal was skipped")
# print(meals)

# comprehension format for the same would be
# so this is like our first comprehension, but the expression part's a bit more complex
# although you can use a function, to avoid excessively complex code.
meals = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
# print(meals)

""" *
    *   writing a complex expression
    * """
for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)
