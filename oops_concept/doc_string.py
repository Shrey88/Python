# ================================================================
# so we are going to work with a record collection to show how classes can be
# used together.
#
# ================================================================

class Song:
    """
        Class to represent a song

        Attributes:
            title (str): title of the song
            artist (Artist): object representing the songs creator
            duration (int): duration of the song in seconds, may be zero.
    """
    def __init__(self, title, article, duration=0):
        """
            Song init method
            :param title: initializes the 'title' attribute
            :param article: Artist object representing the song's creator.
            :param duration: initial value for the 'duration' attribute.
                            will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


"""
    so help function will print the doc strings mentioned for class and its method 
"""
# print("displays the doc string for the class and its method:")
# help(Song)
# print()


"""
    to display the doc string for the method, you can mention the class-name.method-name
"""
# print("displays the doc string for method-name that is mentioned:")
# help(Song.__init__)
# print()


"""
    to display only the doc string for the class
"""
# print("displays the doc string for class")
# print(Song.__doc__)
# print()


"""
    in python functions and methods are also objects.
    here we are trying to access the doc attribute of init method.
"""
# print(" displaying the doc string attribute of method")
# print(Song.__init__.__doc__)
""" this is the another way of assigning the documentation """
# Song.__init__.__doc__ = """
#             Song init method
#
#             Args:
#             title: initializes the 'title' attribute
#             article: Artist object representing the song's creator.
#             duration: initial value for the 'duration' attribute.
#                         will default to zero if not specified.
#         """
# help(Song)
# print()
