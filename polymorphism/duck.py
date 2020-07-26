"""
    Polymorphism:
    if we write a function that accepted and Enemy as a parameter and called the take_damage method of its parameter, there's no guarantee
    that the object we passed to t would have a take_damage method in Python.We could pass a Player instance to it, for example, and we
    haven't given out Player class that method.

    In java that wouldn't be a problem, we'd have to specify Enemy, say, as the type of the parameter, and the compiler would check that
    anything we passed did inherit from the Enemy class.

    In Python, there's no such checking. Python isn't interested in the type of objects, it's only interested in their behaviour
    at the time they're used.
"""


class Duck(object):

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on itm the water's lovely")

    def quack(self):
        print("Quack, quack")


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)
