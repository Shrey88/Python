# ===============================================================================================================
# tkinter module provides access to the TK widget tool kit
# it allows gui program to be created
# TK toolkit was developed to work with scripting language called TCL and tkinter python binding works by actively
# sending TCL code to a TCL interpreter but that's actually embedded in the python interpreters.
# python has graphics libraries available other than tkinter, but tkinter has advantage that, it's part of
# standard python language and therefore it is available without installing anything
# but also has a disadvantage in that the documentation isn't brilliant
# ===============================================================================================================

# =============================================
# if you are running python 3 then the import line from try block will be executed
# and if you are running python 2 then the import line from except block will be executed
# =============================================
try:
    import tkinter
except ImportError:  # python2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# ==================================
# we are calling the protected method from tkinter
# ==================================
# tkinter._test()


# ==================================
# creating a window
# ==================================
mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
# =======================================
# it is the size of the window
# it accepts the string instead of numbers
# the width and height are separated by x
# here the window is 100 pixel in from the left edge of the screen and
# 400 pixel down now.
# if you use - instead of + then we will get 100 pixel in from the right edge of the screen and
# 400 pixel up from the bottom.. you can mix plus and minus.
# =======================================
mainWindow.geometry("640x480-100-400")
mainWindow.mainloop()
