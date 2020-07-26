# ==========================================================================================================
# everything in tk is window and objects are placed in a hierarchy
# on screen main window is the root window, so everything must be placed within it or within one of the
# child window.
# not every window can have children but every window except the root one  must have a master window
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
# so to layout the canvas and buttons in managed manner
# we are making use of frame
# ==================================================
leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

# ==================================================
# fill is used to expand the canvas across the screen width
# so when side is set to left and fill is set to vertical expansion i.e. tkinter.Y, then canvas expands vertically but
# when fill is set to horizontal expansion i.e. tkinter.X, then canvas doesn't expand,
# but it will expand only when expand is set to True in canvas.pack
# to test the canvas.pack uncomment it one at a time and execute it.
# now we have changed the placement of canvas and that is from mainWindow to leftFrame
# ===================================================
# canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left')


# ========================================================
# we are adding buttons
# now we are changing the placement of canvas and that is from mainWindow to rightFrame
# ========================================================
# button1 = tkinter.Button(mainWindow, text="button1")
# button2 = tkinter.Button(mainWindow, text="button2")
# button3 = tkinter.Button(mainWindow, text="button3")
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")

# =======================================================
# the widgets share the same side as they are placed adjacent to each other in the order
# that they are actually packed.
# we can change the position of the button by setting the anchor in the button.pack
# here anchor supports compass direction i.e.
#   n - North
#   ne - North-East
#   e - East
#   se - South-East
#   s - South
#   sw - South-West
#   w - West
#   nw - North-West
#   center - for center position
#
# as we have added the buttons in frame, we have removed the anchor from button.pack
# =======================================================
# button1.pack(side='left', anchor='n')
# button2.pack(side='left', anchor='s')
# button3.pack(side='left', anchor='e')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()
