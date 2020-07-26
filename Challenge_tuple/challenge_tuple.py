# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them( remember that you can pass
# more than one item to print function , separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

title, artist, year, tracks = imelda

print("Title: ", format(title))
print("Artist: ", format(artist))
print("Year: ", format(year))
for song in tracks:
    track_no, track_title = song
    print("Track No : {0} \t Tack Name: {1}".format(track_no,track_title))
