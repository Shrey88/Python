# ==================================================================================================
#
# ==================================================================================================
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry("640x480-100-200")
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=5)


# =======================================
# Column Configuration
# =======================================
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
# mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=3)
# mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=3)
# mainWindow.columnconfigure(4, weight=1)


# =======================================
# Row Configuration
# =======================================
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
# mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
# mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=3)
# mainWindow.rowconfigure(4, weight=1)


# ======================================
# File List
# the first argument to fileList.insert is the insertion point
# here we are using the constant tkinter.END, to insert the string to the end of the list
# ======================================
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in sorted(os.listdir('/usr/bin')):  # '/Windows/System32'
    fileList.insert(tkinter.END, zone)

# command is nothing but the action associated with widgets and UI events
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)

# linking the scroll bar to the list box using the y scroll command option
fileList['yscrollcommand'] = listScroll.set


# ======================================
# Frame for the radio buttons.
# ======================================
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='new')

rbValue = tkinter.IntVar()
rbValue.set(0)

# Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')


# =====================================
# Result Label
# widget to display the result
# =====================================
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')


# ======================================
# Frame for the time spinners
# ======================================
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')

# =======================================
# Time Spinners
# you can define the range of values with range() option and inserting it to tuple.
# there is another way of defining it and that is making the use of "from_" and "to"
# if you are wondering why the underscore in the end, because to get around that restriction that reserved word
# widget has an option to set padding for their contents using padx and pady
# padx takes care of left and right padding
# pady takes care of top and bottom padding
# =======================================
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
tkinter.Label(timeFrame, text='Hr').grid(row=0, column=0)
tkinter.Label(timeFrame, text='Min').grid(row=0, column=2)
tkinter.Label(timeFrame, text='Sec').grid(row=0, column=4)
hourSpinner.grid(row=1, column=0)
tkinter.Label(timeFrame, text=':').grid(row=1, column=1)
minuteSpinner.grid(row=1, column=2)
tkinter.Label(timeFrame, text=':').grid(row=1, column=3)
secondSpinner.grid(row=1, column=4)

timeFrame['padx'] = 36


# ==========================================
# Date Frame
#
# ==========================================
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
# dateFrame['padx'] = 30

# Date Labels
dayLabel = tkinter.Label(dateFrame, text="Day").grid(row=0, column=0, sticky='w')
monthLabel = tkinter.Label(dateFrame, text="Month").grid(row=0, column=1, sticky='w')
yearLabel = tkinter.Label(dateFrame, text="Year").grid(row=0, column=2, sticky='w')

# Date Spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                                                        "Oct", "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)


# ======================================
# Buttons
# we should use destroy instead of quit
# destroy actually stops the main loop and deletes the widget and all child widgets
# quit method also stops the TCL interpreter so you may have problems if you are on your program in idle.
# ======================================
okButton = tkinter.Button(mainWindow, text="Ok")

# when we use the parenthesis after the function for e.g. mainWindow.quit(),
# then we are actually calling the function and the result of the function is assigned to the command property
# we don't want the function to run we are assigning the function to be called when the button is click.
# cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.quit)
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.destroy)

okButton.grid(row=4, column=3, sticky='ew')
cancelButton.grid(row=4, column=4, sticky='ew')

mainWindow.mainloop()
