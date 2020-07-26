""" ==================================================================================
====================================================================================== """

import os
import fnmatch  # <-- file name match module is used to match files whose names follow some sort of pattern

""" *
    *   _ mentioned here is to show that you are not using a valley but have to specify value when doing things like 
    *   packing a top all or dealing with values returned by function call.
    *   for this example we return a tuple containing the album name and the path to songs
    * """
def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        # so here we are filtering out the directory names that match the given artist name
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path,artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album),album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):  # <-- we want the path, not the name of the album
            yield song

""" *
    *   so even the wild card character * works with the filter method of fnmatch
    *   so the search string depends on the operating system like if you provide the search string all in lower case 
    *   then also it will return the same result
    *   but the same is not true with the ubuntu or mac system as it is case sensitive search.
    * """
albums_list = find_albums(".\music", "Black*")
song_list = find_songs(albums_list)

for s in song_list:
    print(s)