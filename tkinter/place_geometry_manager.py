# ==========================================================================================
# widgets in the same column can be lineup above or below each other
# widgets in the same row can be lined up next to each other.
# we will be making use of grid instead of pack.
# ==========================================================================================

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480-100-200")

label = tkinter.Label(mainWindow, text="Hello World")
# label.pack(side='top')
label.grid(row=0, column=0)

# ==================================================
# so to layout the canvas and buttons in managed manner
# we are making use of frame
# to make the position of the buttons more accurate, we are using sticky option inside the grid
# sticky can have following string values for positioning
# you can use make use of multiple combinations with the compass points in sticky option
# i.e. you can mention nwe, nsw... etc.
#   n - North
#   e - East
#   s - South
#   w - West
#   center - for positioning it in center
# default option for sticky is center.
# ==================================================
leftFrame = tkinter.Frame(mainWindow)
# leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
leftFrame.grid(row=1, column=1)

rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='right', anchor='n', expand=True)
rightFrame.grid(row=1, column=2, sticky='n')
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
# canvas.pack(side='left')
canvas.grid(row=1, column=0)


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
# button1.pack(side='top')
# button2.pack(side='top')
# button3.pack(side='top')
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)


# ==========================================================
# column configure
#
# ==========================================================
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

# ==========================================================
# Frame configure
# the row height is now determined by the height of the tallest widget it contains.
# ==========================================================
leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

# ==========================================================
# Button Config
# we will try to increase the width of the button to the full width of the frame by
# setting the sticky option
# so after executing the you will see no difference in the button width
# that's because of the weight option, which plays important role in deciding the behavior of widgets within cells
# so unless a weight has been set for a column or row, then some options including sticky won't do anything
# the right frame has only one column so if we set its weight first, then button2 sticky option will work.
# ==========================================================
rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')
mainWindow.mainloop()
