"""
   Composition: (has a relationship)

"""


class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    """
    here we have created the object of Wing class and assigned it to the attribute _wing of Duck class
    now any Duck objects we create will have their own wing object, and it can now use the attributes of Wing along
    with the fly method.

    so when a class contains the another object like this is called composition.
    """
    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on itm the water's lovely")

    def quack(self):
        print("Quack, quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")


if __name__ == '__main__':
    donald = Duck()
    donald.fly()

