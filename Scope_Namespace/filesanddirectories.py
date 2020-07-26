# ======================================================================
# using operating system api's to print the directory and files inside it
# ======================================================================

import os


# listing = os.walk('.')  # we have provided the current location i.e the project path
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for file in files:
#         print(file)


# ================================================================
# nesting one function into another function
#
# global keyword tell Python to look for a variable in the global scope which is the modules name space
# non local keyword tell it to look fo that variable in the enclosing scopes
# (in this program it is asking to look in an enclosing function )
# ================================================================


def list_directories(s):

    def dir_list(d):
        """ Even after declaring the variable as global it was still not resolving the issue
        that tab_stop is not defined.
        their are ways to get out of it by creating the global variable but the Python3
        introduces another way to  specify the scope of a variable in situations like this
        so we need to change the global reference to nonlocal"""
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + "does not exist")


list_directories('.')
