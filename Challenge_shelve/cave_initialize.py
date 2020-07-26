# ========================================================
# creating shelve
# ========================================================
import shelve

locations = shelve.open("location")
# locations["0"] = {"desc": "You are sitting in front of a computer learning Python",
#                  "exits": {},
#                  "name_exits": {}}
# locations["1"] = {"desc": "You are standing at the end of a road before a small brick building",
#                  "exits": {"W": "2", "E": "3", "N": "5", "S": "4", "Q": "0"},
#                  "name_exits": {"2": "2", "3": "3", "5": "5", "4": "4"}}
# locations["2"] = {"desc": "You are at the top of a hill",
#                  "exits": {"N": "5", "Q": "0"},
#                  "name_exits": {"5": "5"}}
# locations["3"] = {"desc": "You are inside a building, a well house for a small stream",
#                  "exits": {"W": "1", "Q": "0"},
#                  "name_exits": {"1": "1"}}
# locations["4"] = {"desc": "You are in a valley beside a stream",
#                  "exits": {"N": "1", "W": "2", "Q": "0"},
#                  "name_exits": {"1": "1", "2": "2"}}
# locations["5"] = {"desc": "You are in a forest",
#                  "exits": {"W": "2", "S": "1", "Q": "0"},
#                  "name_exits": {"2": "2", "1": "1"}}

locations.close()

direction_keys = shelve.open("direction_key")
# direction_keys["NORTH"] = "N"
# direction_keys["SOUTH"] = "S"
# direction_keys["EAST"] = "E"
# direction_keys["WEST"] = "W"
# direction_keys["QUIT"] = "Q"
# direction_keys["ROAD"] = "1"
# direction_keys["HILL"] = "2"
# direction_keys["BUILDING"] = "3"
# direction_keys["VALLEY"] = "4"
# direction_keys["FOREST"] = "5"
direction_keys.close()
