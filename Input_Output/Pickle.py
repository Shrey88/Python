# =============================
# python provides a mechanism for serializing objects called Pickling, hence called pickle
# when object is pickled, it's written to a file  and format that contains the object
# data together with sufficient information to allow that object to be recreated when it's loaded back in
# it takes care about the data, so that loading the data can be done easily.
# unpickling the data from the other sources(which cannot be trusted) should not be done
# when dumping the data to file you an specify the protocol = <protocol_ver>
# as an argument to pickle.dump()
# or you can also use the in-built protocols
# i.e. pickle.DEFAULT_PROTOCOL or pickle.HIGHEST_PROTOCOL
# protocols is used when you want to write the data and read the data in same format
# =============================


import pickle  # library

imelda=("More Mayhem", "Imelda May", "2011", ((1, "Pulling the Rug"), (2, "Pyscho"),
          (3, "Mayhem"), (4, "Kentish Town Waltz")))
#
# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda,pickle_file)


# ===============================
# loading the pickle data
# ===============================

# with open("imelda.pickle", "rb") as pickle_file:
#     imelda2 = pickle.load(pickle_file)
#     print(imelda2)
#
# album, artist, year, track_list = imelda2
# track1, track2, track3, track4 = track_list
#
# print("Album : ", album)
# print("Artist : ", artist)
# print("Year : ", year)
# print("Tack1 : ", track1)
# print("Track2 : ", track2)
# print("Track3 : ", track3)
# print("Track4 : ", track4)


# ===============================
# 2nd example
# Writing and Reading pickle objects
# ===============================

# *****************Writing********************
# with open("imelda.pickle", "wb") as pickle_file:
#     even = list(range(0, 10, 2))
#     odd = list(range(1, 10, 2))
#     pickle.dump(even, pickle_file)
#     pickle.dump(odd, pickle_file)
#     pickle.dump(imelda, pickle_file)
#     pickle.dump(2998324, pickle_file)

# *****************Reading********************
# with open("imelda.pickle", "rb") as pickle_file:
#     even_list = pickle.load(pickle_file)
#     odd_list = pickle.load(pickle_file)
#     imelda2 = pickle.load(pickle_file)
#     number = pickle.load(pickle_file)
#
# album, artist, year, track_list = imelda2
# track1, track2, track3, track4 = track_list
#
# print("Album : ", album)
# print("Artist : ", artist)
# print("Year : ", year)
# print("Tack1 : ", track1)
# print("Track2 : ", track2)
# print("Track3 : ", track3)
# print("Track4 : ", track4)
# print("Even : ", even_list)
# print("Odd : ", odd_list)
# print("Number : ", number)


# ===============================
# deleting the file
# ===============================
# pickle.load(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")  # Mac/Linux
# pickle.load(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")  # Windows
