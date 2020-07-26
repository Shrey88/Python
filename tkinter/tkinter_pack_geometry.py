# ==========================================================================================================
# everything in tk is window and objects are placed in a hierarchy
# on screen main window is the root window, so everything must be placed within it or within one of the
# child window.
# not every window can have children but every window except the root one  must have a master window
# pack is for very simple layouts
# side= works only for the pack.
# ==========================================================================================================

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480+100+400")

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

# ==================================================
# fill is used to expand the canvas across the screen width
# so when side is set to left and fill is set to vertical expansion i.e. tkinter.Y, then canvas expands vertically but
# when fill is set to horizontal expansion i.e. tkinter.X, then canvas doesn't expand,
# but it will expand only when expand is set to True in canvas.pack
# to test the canvas.pack uncomment it one at a time and execute it.
# ===================================================
canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
# canvas.pack(side='left', fill=tkinter.Y)
# canvas.pack(side='left', fill=tkinter.X, expand=True)
# canvas.pack(side='right', fill=tkinter.Y)
# canvas.pack(side='right', fill=tkinter.X, expand=True)
# canvas.pack(side='top', fill=tkinter.X)
# canvas.pack(side='top', fill=tkinter.Y, expand=True)
# canvas.pack(side='bottom', fill=tkinter.X)
# canvas.pack(side='bottom', fill=tkinter.Y, expand=True)

# =========================================================
# the below ones are similar to the above ones, the only difference is of the constant i.e. BOTH
# to test the below canvas.pack, uncomment it one at a time and execute it.
# =========================================================
# canvas.pack(side='left', fill=tkinter.BOTH)
# canvas.pack(side='left', fill=tkinter.BOTH, expand=True)
# canvas.pack(side='right', fill=tkinter.BOTH)
# canvas.pack(side='right', fill=tkinter.BOTH, expand=True)
# canvas.pack(side='top', fill=tkinter.BOTH)
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)
# canvas.pack(side='bottom', fill=tkinter.BOTH)
# canvas.pack(side='bottom', fill=tkinter.BOTH, expand=True)


mainWindow.mainloop()