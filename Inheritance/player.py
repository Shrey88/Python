class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    """
        by declaring the variable name with an underscore they are not really hidden as such,
        but there's no need for clients to use them directly.
        
        underscore at the start of the method name gives the users of our class an indication
        that they shouldn't really be calling these methods.
        
        we will add some validation to the setter method
        
        so although setter aren't needed as such in python, they're very useful when you'd want to 
        include the validation on the values that your data attributes can be set to 
    """
    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    """
        we will define a property called lives that uses these two method names
        when reading and writing our lives attribute.

        we have replaced the attribute underscore lives with a property called lives.
        so need to make any change in the main class.

        data attribute mustn't have the same name as the property

        name of the property equals to the call to the properties class constructor
        to create a new property.

        so if you don't specify a method to use for the setter then the property is gonna be read only
        which is sometimes useful.

        and if you specify setter byt no getter then you can change the value of the property but you can't 
        display it and that's really the less useful , possibly may be for a password attribute.
    """
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    """
        so we have mentioned @property so this is the alternative to the defining the property in the above line
        this is called as decorators.
        
        so we have created a setter which is similar to the other setters defined above only the difference is 
        we have mention the decorator for it i.e. @property_name followed by dot setter
    """
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
    """
        this is a STI method
        we are overwriting the object method here 
    """
    def __str__(self):
        return "Name: {0.name}, Lives:{0.lives}, Level: {0.level}, Score: {0.score}".format(self)



