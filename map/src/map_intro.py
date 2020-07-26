""" ********************************************************
    Map Intro

    so map takes two arguments:
        1:  is a function and we have used the upper function from string class
        Note:   when passing the function as an argument you don't have to include the opening and
                closing parentheses.
                when you use the parentheses you're passing the result of the calling function, but here
                we want to pass the function itself.

        2:  the second argument is the iterator, you can use anything that can be iterated over such as
            string or a list.
************************************************************ """

text = "what have the romans ever done for us"

# Comprehension format
capitals = [char.upper() for char in text]
print(capitals)

# map format
map_capitals = list(map(str.upper, text))
print(map_capitals)

# Comprehension format
words = [word.upper() for word in text.split(' ')]
print(words)

# map format
map_words = list(map(str.upper, text.split(' ')))
print(map_words)

