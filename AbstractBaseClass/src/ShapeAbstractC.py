""" *
    *   Abstract class is which does not have a definition on its own.
    *
    *   it has abstract methods which forces the implementation in its derived classes.
    *   """
from abc import ABCMeta, abstractmethod

""" *
    *   here we are making the class shape as an instance of the class ABCMeta
    *   ABCMeta is a class which has the properties of an abstract base class.
    *   """


class ShapeAbstractC(metaclass = ABCMeta):

    @abstractmethod
    def area(self):
        return 0


class Square(ShapeAbstractC):
    side = 4

    def area(self):
        print("Area of square : ", self.side * self.side)


class Rectangle(ShapeAbstractC):
    width = 5
    length = 10

    def area(self):
        print("Area of rectangle : ", self.width * self.length)


square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()

# you cannot create an object/instance of the abstract class
shape = ShapeAbstractC()