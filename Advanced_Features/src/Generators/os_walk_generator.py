""" ===========================================================================
    OS Walk Generator
==============================================================================="""
import os

""" *
    *   how we can access files on computer's hard disk
    *   the os.walk function can be used to recursively retrieve the contents of a directory as well as all its 
    *   subdirectories.
    *   
    *   os.walk is generator, so it doesn't put up a huge list of all the files and directories on the hard drive
    *   it just returns them as needed.
    *
    *   os.walk returns the list 
    * """

root = ".\music"

# for path, directories, files in os.walk(root, topdown=True):
#     print(path)
#     for f in files:
#         print("\t{}".format(f))


""" *
    *   the below code is to understand how the above code flows.
    *
    *   so if you see it will first enter into the music folder and list down the sub-directories and files present in it if any
    *   On the first enter... it will enter into the sub-folder(the selection will be based on the ascending order of the folder name)
    *   so it follows the topdown methodology where it even covers the sub-directories
    *   it also does the backtracking where if you have reached the leaf node in one folder it will come out of the folder and try to 
    *   traverse the another folder.
    * """
# for path, directories, files in os.walk(root, topdown=True):
#     print("Path : ",path)
#     print("Directory : ",directories)
#     print("Files : ",files)
#     input("Press Enter.....")

""" *
    *   to split the path, it will enter into if condition only if that folder has files
    *   splits the path by getting the string after last slash using tail keyword and returns the tuple with two strings
    * """
# for path, directories, files in os.walk(root, topdown=True):
#     if files:
#         print(path)
#         first_split = os.path.split(path)
#         print(first_split)
#         print('=' * 30)

""" *
    *   so what is observed with the strip is that it is removing not only the complete matching string but
    *   but also the matching character from the strip string with the tuple values.
    *   for example if it is suppose to list '3', 'Mushmouth Shoutin' it will strip 3 as well in the final list
    *   another example if it is suppose to list '8', 'La Grange' as the final string but it will strip e which is the last character of Grange
    *   resulting into '8', 'La Grang' as the final string
    * """
# for path, directories, files in os.walk(root, topdown=True):
#     if files:
#         print(path)
#         first_split = os.path.split(path)
#         print(first_split)
#         second_split = os.path.split(first_split[0])
#         print(second_split)
#         for f in files:
#             song_details = f.strip('.emp3').split('-')
#             print(song_details)
#         print('=' * 30)


""" *
    *   so to overcome the above problem we will split the string using the usual way of splitting the last 5 characters
    * """
for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f[:-5].split('-')
            print(song_details)
        print('=' * 30)