# ===========================================================================================
# Everything in Python is an object i.e. even types are implemented as classes
#
# attributes - when a variable is bound to an instance of a class then it's referred to as a data attribute in Python
# fields in java
# data members in C++
# ===========================================================================================


class Kettle(object):

    power_source = 'electricity'

    def __init__(self, make, price):  # constructor
        self.make = make
        self.price = price
        self.on = False

    """
        the main difference between the function and method is the 
        presence of this "self" parameter that's been added automatically 
        
        "self" is the reference to the instance of the class now, it is equivalent to
        "this" in C++/Java
    """
    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))


# ==============================================================================================
# as kenwood and hamilton are objects we can specify their attributes in the replacement fields
# ==============================================================================================
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print("Hamilton:")
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# =============================================================================================
# we are using the class itself instead of using the instance of kettle to call a method
# because there is no instance here the value for self has to be specified and failing to do so would give an error
#
# =============================================================================================
print("Kenwood")
Kettle.switch_on(kenwood)
print(kenwood.on)


# =============================================================================================
# when variables come into existence the first time, they are assigned a value
# and the same thing is true for instance variables.
# power is the attribute that is bound to an instance of the kettle class i.e kenwood
# if you try to access power attribute with the hamilton then it will throw error
# this is the dynamic nature of Python that allows this kind of behaviour, it is a useful feature
# but can cause problems if you make a typing error.
# here the power attribute is available with only the kenwood instance of kettle.
# =============================================================================================
kenwood.power = 1.5
print(kenwood.power)

# ===============================================
# so it is clear that both the instances are looking for the class variable
# ===============================================
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

# ===============================================
# we will change the value of power_source for kettle, kenwood and hamilton
# so when you assign the new value to global variable, Python creates a nes local variable that shattered the global one
#
# ===============================================
Kettle.power_source = "atomic"
print("Kettle power source: {}".format(Kettle.power_source))

kenwood.power_source = "water"
print("Kenwood power source: {}".format(kenwood.power_source))

hamilton.power_source = "gas"
print("Hamilton power source: {}".format(hamilton.power_source))


# =============================================
# to check the namespace use __dict__
# =============================================
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)


# ============================================
# encapsulation is that objects contain the data and methods that operate on that data and don't expose
# the actual implementation to the outside world
# modular2 aimed to provide encapsulation by using modules rather than objects
#  modular2 was enhance to become modular3
# Python allows us to encapsulate data methods using either an object orientated paradigm or a modular approach
# ============================================
