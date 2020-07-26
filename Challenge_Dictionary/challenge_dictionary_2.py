# Challenge time
# We have modified that the data for the Adventure game could be organised in many
# different ways. We've created another way for you.
# Your mission , if you choose to accept it , is to
# change the code to make it work.
# Below is the complete program from that ast video, both with the
# locations dictionary modified so tat everything is in a single dictionary.
# N.B. Yes the coded has some errors, that's what you need to fix!

locations = {0: {"desc": "You are sitting in front of a computer learning Python",
                 "exits": {},
                 "name_exits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "name_exits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "name_exits": {"5": 5}},
             3: {"desc": "You are inside a building, a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "name_exits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "name_exits": {"1": 1, "2": 2}},
             5: {"desc": "You are in a forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "name_exits": {"2": 2, "1": 1}}
             }

direction_key = {"NORTH": "N",
                 "SOUTH": "S",
                 "EAST": "E",
                 "WEST": "W",
                 "QUIT": "Q",
                 "ROAD": "1",
                 "HILL": "2",
                 "BUILDING": "3",
                 "VALLEY": "4",
                 "FOREST": "5"}
loc = 1

while True:
    availableExits = ", ".join(locations.get(loc).get("exits").keys())
    print(locations.get(loc).get("desc"))

    if loc == 0:
        break
    else:
        allExits = locations.get(loc).get("exits").copy()
        allExits.update(locations.get(loc).get("name_exits"))

    direction = input("Available exits are " + availableExits + ": ").upper()
    print()
    if direction_key.get(direction) in allExits.keys():
        loc = allExits.get(direction_key.get(direction))
    elif direction in allExits.keys():
        loc = allExits.get(direction)
    else:
        print("You cannot go in that direction")
