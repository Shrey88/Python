class Song:
    """
        Class to represent a song

        Attributes:
            title (str): title of the song
            artist (Artist): object representing the songs creator
            duration (int): duration of the song in seconds, may be zero.
    """
    def __init__(self, title, artist=None, duration=0):
        """
        Song init method
        :param title: (str): initializes the 'title' attribute
        :param artist: (Artist): Artist object representing the song's creator.
        :param duration: (int): initial value for the 'duration' attribute.
                        will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """
        Class to represent an Album, using it's track list

        Attributes:
            name: (str): the name of the album.
            year: (int): the year album was released.
            artist: (Artist): The artist responsible for the album, if not specified,
                            the artist will default to an artist with the name "Various Artists"
            tracks: (List(Song)): A list of the songs on the album.

        Methods:
            add_Song: used to add a new song to the album's track list.s
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """
            Adds a song to the track list

            :param song: (Song): A Song to add
            :param position: (Optional(int)): If specified, the song will be added to that position in the track list
                                            inserting it between other songs if necessary .
                                            Otherwise, the song will be added to the end of the list.
            :return:
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


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


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums/albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of {artist, album, year, song}
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # store the current album in the currents artists collection then create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # We've just read a new album for the current artist
                # store the current album in the artist's collection then create a new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After reading the last line of the text file, we have an artist and album that haven't
        # been store - process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))
