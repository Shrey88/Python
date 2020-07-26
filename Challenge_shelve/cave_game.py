# ===================================================
# ===================================================

import shelve

loc = "1"
locations = shelve.open("location")
direction_key = shelve .open("direction_key")
while True:
    availableExits = ", ".join(locations.get(loc).get("exits").keys())
    print(locations.get(loc).get("desc"))

    if loc == "0":
        break
    else:
        allExits: object = locations.get(loc).get("exits").copy()
        allExits.update(locations.get(loc).get("name_exits"))

    direction = input("Available exits are " + availableExits + ": ").upper()
    print()
    if direction_key.get(direction) in allExits.keys():
        loc = allExits.get(direction_key.get(direction))
    elif direction in allExits.keys():
        loc = allExits.get(direction)
    else:
        print("You cannot go in that direction")

locations.close()
direction_key.close()
