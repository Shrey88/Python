"""
    this code is to demonstrate inheritance

    Inheritance is - is a relationship
"""
import random


"""
    Refactoring the variable name will not take reflect in string.
    for e.g. if the variable name is used like {0.name} to change it to new name use regular expression
    in replace command window
    in search field - (\{\d\.)
    in replace field - $1._  
    
"""


class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1

            if self._lives > 0:
                print("{0._name} lost a little".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


"""
    so we are inheriting the Enemy class into Troll class or you can say Troll class extends the Enemy class,
    this is how the inheritance declaration looks like
    
    there is a very useful command called pass that doesn't do anything, so basically after declaring class it
    expects the code and will show syntax error so to remove that error we have typed in --> pass, which allows
    you to run your code.
"""


class Troll(Enemy):

    """
        this will give you error saying that Troll does not have name attribute in it, because python no longer points
        to the init method of enemy class instead it is poiting to the init method of the troll class

        so what we actually need to do is to call the init method of the superclass inside the troll's init method

    """
    def __init__(self, name):
        """
            here we are prefixing the method name with the class name
            this is the one way of doing it in Python 2
        """
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)

        """
            here we will use the keyword super to call the method of the superclass
            this sytax is followed in Python 3
            
            here we are passing the name of the class and instance of the class troll
        """
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)

        """
            this is the shorthand of above command
        """
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0._name}, {0._name} stomp you".format(self))


class Vampire(Enemy):

    def __init__(self, name, hit_points):
        # super().__init__(name=name, lives=3, hit_points=12)
        super().__init__(name=name, lives=3, hit_points=hit_points)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampyreKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name, hit_points=140)

    def take_damage(self, damage):
        super().take_damage(damage=(damage//4))
