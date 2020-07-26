# Sets are unordered collections
# it guarantees that it will not have duplicates in collection
# Sets are similar to list in that they 'are actually intended to store similar items
# You can't actually access individual items using an index, as the sets is unordered
# SET is probably more similar to collection of dictionary keys
# SET members are hashed in the same ways dictionary keys are.
# Elements in set must be immutable objects

# =====================================
# first way of defining the set
# =====================================
# farm_animals = {"sheep", "cow", "hen"}
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)

# ====================================
# second way of defining the set
# ====================================

# wild_animals = set(["Lion", "Tiger", "Panther", "Elephant"])
#
# print(wild_animals, '\n')
#
# for animal in wild_animals:
#     print(animal)


# ===================================
# Adding new data to the sets defined
# ===================================
# farm_animals.add("horse")
# wild_animals.add("horse")
#
# print(farm_animals)
# print(wild_animals)


# ===================================
# Creating empty set
# Recommended: use set constructor for defining the set
# ===================================
# empty_set = set()
## empty_set2 = {}  # this line actually creates a dictionary
# empty_set.add("a")
## empty_set2.add("a")  # as empty_set2 creates dictionary, dictionary does not have add method

# ===================================
# Other way of defining set
# ===================================
even = set( range( 0, 40, 2 ) )
# print( even )
# print( len( even ) )

square_tuple = (4, 9, 16, 25)
squares = set( square_tuple )  # tuple can also be used to generate set.
# print( squares )
# print( len( squares ) )

# ===================================
# Union of sets (even and square)
# ===================================
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
# print(len(squares.union(even)))


# ===================================
# Intersection of sets (even and square)
# ===================================
# print(even.intersection(squares))
# print(squares.intersection(even))

# other way is using & ampersand sign.
# it internally uses .intersection method
# print(even & squares)
# print(squares & even)


# ===================================
# Subtraction of sets (even and square)
# so it is like subtracting set B from A, where the elements from set B present in set A are removed
# ===================================
# print( sorted( even ) )
# print( sorted( squares ) )

# subtracting even from square
# print("# ===================================")
# print("# Subtracting even from squares")
# print("# ===================================")
# print(even.difference(squares))
# print (even - squares)  # - sign internally calls ".difference" method

# subtracting square from even
# print("# ===================================")
# print("# Subtracting squares from even")
# print("# ===================================")
# print(squares.difference(even))
# print (squares - even)  # - sign internally calls ".difference" method


# ===================================
# Update Subtraction of sets (even and square)
# so it is like subtracting set B from A, where the elements from
# set B present in set A are removed from set B permanently.
# ===================================
# even.difference_update(squares)
# print(sorted(even))

# ===================================
# Symmetric difference of 2 sets.
# all the members that are present in one set or the other but not both.
# removing the common elements from both and merging the left out elements.
# output will be identical in both the cases
# even.symmetric_difference(squares)
# squares.symmetric_difference(even)
# ===================================
# print( sorted( even.symmetric_difference( squares ) ) )
#
# print( sorted( squares.symmetric_difference( even ) ) )

# symmetric difference can also be represented in form of carrot sign
# print(sorted(even ^ squares))
# print(sorted(squares ^ even))


# ===================================
# Two ways to remove element from set
# discard : it will not throw an error if the element is not present in the set.
# remove : it will throw an error when trying to remove an element not present in the list.
# ===================================
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  # does not give error, as it does nothing

# Recommendation: if you are using remove method its better to check first,
# whether the element exist in set or not.
#squares.remove(8)

# if(8 in squares):
#     squares.remove(8)

# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not member of set")
#
# print(squares)

# ===================================
# Subset : if all the elements of one set are present in another set.
# Superset : if all the elements from one set are available in another set.
# ===================================
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(squares)
#
# if squares.issubset(even):
#     print("squares is a subset of even")
#
# if(even.issuperset(squares)):
#     print("even is a superset of square")


# ===================================
# Frozen set:
# it is immutable
# we can use it as dictionary key.
# once created cannot be changed
# ===================================
even = frozenset(range(0, 100, 2))
print(even)
even.add(3)  # it does not have add method, so this line will throw error.
