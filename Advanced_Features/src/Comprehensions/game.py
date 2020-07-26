locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are insided a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}
         }

loc = 1
# normal way of writing the code
# for xit1 in exits:
#     if loc in exits[xit1].values():
#         print(locations[xit1])

# Comprehension way of writing the code
# forest = [locations[xit2] for xit2 in exits if loc in exits[xit2].values()]
# print(forest)

# normal way of writing the code to iterate through all the locations
for loc in sorted(locations):
    for xit3 in exits:
        if loc in exits[xit3].values():
            print((xit3, locations[xit3]), end='\t')
    print()

# comprehension way of writing the code to iterate through all the locations
for loc in sorted(locations):
    forest = [(xit4, locations[xit4]) for xit4 in exits if loc in exits[xit4].values()]
    print("Locations leading to {}".format(loc), end='\t')
    print(forest)