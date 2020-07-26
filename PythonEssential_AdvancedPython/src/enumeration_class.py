from enum import Enum, unique, auto

""" *
    *   enum has both name and value property
    *   you cannot have same enum name but you can have same value for different enum name which is also treated as key
    *   you can prevent duplicate values vy using the unique decorator.
    *   you need to mention @unique before declaring enum.
    *   you can use auto function to automatically assign value to enum and to do that we ned to import auto code from 
    *   enum package 
    * """
@unique  # <-- decorator for avoiding duplicate enum value
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()


def main():
    # enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # print the auto-generated value
    print(Fruit.PEAR.value)

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])


if __name__ == "__main__":
    main()
