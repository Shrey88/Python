# from player import Player
from enemy import Enemy, Troll, Vampire, VampyreKing

"""
    the below code is for the Player class
    header for this code is --> from player import Player
"""
# tim = Player("Tim")

# print(tim.name)
# print(tim.lives)
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)

# tim.level = 2
# print(tim)
#
# tim.level = 5
# print(tim)
#
# tim.level = 3
# print(tim)
#
# tim.score = 500
# print(tim)

"""
    the below code is for enemy class which is to demonstrate the inheritance
    header for this code is --> from enemy import Enemy
"""

# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(8)
# print(random_monster)
#
# random_monster.take_damage(9)
# print(random_monster)

"""
    if the default constructor __init__ is not defined in the class 
    then below code will print the values for the enemy class.
    
    in any other language like C++ or Java we have to declare three constructors one for each case 
    with different input parameters, but python doesn't have the concept of overloaded methods.
"""
# ugly_troll = Troll("Pug")
# ugly_troll.take_damage(4)
# ugly_troll.take_damage(9)
# ugly_troll.take_damage(10)
# ugly_troll.take_damage(11)
# print("Ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))
#
# brother = Troll("Urg")
# print("brother - {}".format(brother))

"""
    before extending the Vampire class
"""
# vampire1 = Vampire("Vampire")
# vampire1.take_damage(5)
# print(vampire1)
#
# while vampire1._alive:
#     vampire1.take_damage(1)
#     # print(vampire1)

vampK = VampyreKing("Vlad")
vampK.take_damage(8)
print(vampK)