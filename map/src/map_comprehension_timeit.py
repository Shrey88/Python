import timeit

text = "what have the romans ever done for us"


# Comprehension format
def char_comprehension():
    capitals = [char.upper() for char in text]
    return (capitals)


# map format
def char_map():
    map_capitals = list(map(str.upper, text))
    return (map_capitals)


# Comprehension format
def word_comprehension():
    words = [word.upper() for word in text.split(' ')]
    return (words)


# map format
def word_map():
    map_words = list(map(str.upper, text.split(' ')))
    return (map_words)


print("char_comprehension : ", timeit.timeit(char_comprehension, number=1000))
print("char_map : ", timeit.timeit(char_map, number=1000))
print("word_comprehension : ", timeit.timeit(word_comprehension, number=1000))
print("word_map : ", timeit.timeit(word_map, number=1000))
