class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

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

    def __init__(self):
        """
            so this the reference of the aviate method that we are assigning to the variable fly
            when the instance/object of penguin class calls pen.fly(), the fly variable which has
            reference to aviate method is de-referenced thus calling the aviate method
        """
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")

    def aviate(self):
        print("I won the lottery and bought a learjet")


class Flock(object):

    def __init__(self):
        self.flock = []

    """
        here we have added a hint saying that duck variable is 
        nothing but the object of Duck class
        
        and as function is not returning anything we have denoted it as "-> None"
    """
    def add_duck(self, duck: Duck) -> None:
        # self.flock.append(duck)  # you can uncomment this line if you want to see the exception when you pass the object of class which is not having the fly method

        # if type(duck) is Duck:  # here we are checking if the duck variable is containing the object of type Duck class
        #     self.flock.append(duck)

        """ this is another way of checking the instance if of specific type """
        # if isinstance(duck, Duck):  # isinstance also does the same thing, it checks if variable duck is of type Duck class or not
        #     self.flock.append(duck)

        """ 
            so here we are checking if the object(duck) has any method
            in getattr (duck, 'fly', None) is equivalent to duck.fly(this fly can contain any method name)
            
            functions and methods are callable 
            
            data attributes aren't callable, that's not strictly true because 
            you can't have a callable data attribute in python
        """
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:  # this is custom exception: we are raising the exception because the object of the class is not having the fly method.
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None

        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:  # so when we use "as e" with the exception it is reference to the exception store in the variable
                print("One duck down")
                # raise  # to raise the exception that we caught just now, type-in raise
                problem = e  # so assign the value of e to a variable and after the for loop is completed check if variable is having any exception and raise it.
        if problem:  # this way is not recommended usually. it's just for the information
            raise


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
