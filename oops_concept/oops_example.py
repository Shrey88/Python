"""
    here we are going to see some oops concept coming into picture.
    you can compare this code with the record_collection_1.py file to understand what changes we did.

    here we are going to delegate the work to a class who is responsible of doing that.
    we have also removed the circular reference.
    Adding the getter and setter method to access the class members.
"""


class Song:
    """
        Class to represent a song

        Attributes:
            title (str): title of the song
            artist (str): The name of the song's creator
            duration (int): duration of the song in seconds, may be zero.
    """

    def __init__(self, title, artist=None, duration=0):
        """
        Song init method
        :param title: (str): initializes the 'title' attribute
        :param artist: (str): The name of the song's creator
        :param duration: (int): initial value for the 'duration' attribute.
                        will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """
        Class to represent an Album, using it's track list

        Attributes:
            name: (str): the name of the album.
            year: (int): the year album was released.
            artist: (str): The name of the artist responsible for the album.If not specified,
                            the artist will default to an artist with the name "Various Artist"
            tracks: (List(Song)): A list of the songs on the album.

        Methods:
            add_Song: used to add a new song to the album's track list.s
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """
            Adds a song to the track list

            :param song: (Song): The title of the song to add.
            :param position: (Optional(int)): If specified, the song will be added to that position in the track list
                                            inserting it between other songs if necessary .
                                            Otherwise, the song will be added to the end of the list.
            :return:
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


"""
    NOTE:

    The major problem with this design is that an artist object will have a reference to an album 
    and that album object will also have a reference to the artist.Now the problems that can cause are to 
    do with garbage collection so when objects are no longer used in your Python code they still take up 
    memory until they're ultimately destroyed.

    Example:
    if we were to create an album object for say adells 25
    it would have a adell as its artist attribute however the adell artist object would have a 25 in its list of albums
    so when the program is no longer using these, the garbage collector might see that there's still a reference to both
    objects each from the other one and then ultimately not reclaim the memory for either, so you can see how would then 
    stall both of those entries sort of permanently well until your program finishes and won't claim the amount of memory 
    space with having said that Python 3 garbage collector is quite advanced.

    This is the best example of circular reference.
"""


class Artist:
    """
        Basic class to store artist details.

        Attributes:
            name: (str): the name of the artist.
            album: (List(Album)) : A list of the albums by this artist.
                                    The list includes only those albums in this collection, it is
                                    not an exhaustive list of the artist's published albums.

        Methods:
            add_album: Use to add a new album to the artist's albums list.
    """

    def __init__(self, name):
        self.name = name
        self.album = []

    def add_album(self, album):
        """
        Add a new album to the list.

        Args:
            :param album: (Album): Album object to add to the list.
                    if the name is already present, it will not be added again (although this is yet to be implemented).
            :return:
        """
        self.album.append(album)

    def add_song(self, name, year, title):
        """
            Add a new song toe collection of albums

            This method will add the song to an album in the collection.
            A new album will be created in the collectin if it doesn't already exist.

            Args:
                name (str): The name of the  album
                year (int): The year the album was produced
                title (str): The title of the son
        """
        album_found = find_object(name, self.album)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)


def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open("albums/albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of {artist, album, year, song}
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))
