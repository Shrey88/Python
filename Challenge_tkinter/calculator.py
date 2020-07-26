# ==========================================================================================================
# write a program to create a single calculator layout
# try to be as Pythonic as possible - it's ok if you end up writing repeated button and grid statements, but consider
# using lists and a for loop.
#
# there is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view
#
# Hint: you may want to use the widgets .winfo_height() and .winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window has been forced to draw the widgets by calling its
# .update() method first.
#
# if you are using Windows you will probably find that the width is already constrained and can't be resized too small
# the height will still need to be constrained though
# ==========================================================================================================

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

from tkinter import font
mainWindow = tkinter.Tk()
# mainWindow.minsize(480, 480)
mainWindow.geometry("480x480+100+200")
mainWindow.title('Calculator')
mainWindow['padx'] = 36
mainWindow['pady'] = 36

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
# mainWindow.columnconfigure(3, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)
mainWindow.rowconfigure(6, weight=1)
mainWindow.rowconfigure(7, weight=1)

inputScreen = tkinter.Entry(mainWindow)
inputScreen.grid(row=0, column=0, columnspan=4, sticky='news')
inputScreen.config(border=0, justify='right')

buttonFont = font.Font(size=12)

cButton = tkinter.Button(mainWindow, text='C')
cButton.grid(row=2, column=0, sticky='news')
cButton.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
               highlightcolor='grey',
               highlightbackground='grey',
               highlightthickness=0)

ceButton = tkinter.Button(mainWindow, text='CE')
ceButton.grid(row=2, column=1, sticky='news')
ceButton.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                highlightcolor='grey',
                highlightbackground='grey',
                highlightthickness=0)

_7Button = tkinter.Button(mainWindow, text='7')
_7Button.grid(row=3, column=0, sticky='news')
_7Button.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                highlightcolor='grey',
                highlightbackground='grey',
                highlightthickness=0)

_8Button = tkinter.Button(mainWindow, text='8')
_8Button.grid(row=3, column=1, sticky='news')
_8Button.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                highlightcolor='grey',
                highlightbackground='grey',
                highlightthickness=0)

_9Button = tkinter.Button(mainWindow, text='9')
_9Button.grid(row=3, column=2, sticky='news')
_9Button.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                highlightcolor='grey',
                highlightbackground='grey',
                highlightthickness=0)

_plusButton = tkinter.Button(mainWindow, text='+')
_plusButton.grid(row=3, column=3, sticky='news')
_plusButton.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                   highlightcolor='grey',
                   highlightbackground='grey',
                   highlightthickness=0)

_4Button = tkinter.Button(mainWindow, text='4')
_4Button.grid(row=4, column=0, sticky='news')
_4Button.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                highlightcolor='grey',
                highlightbackground='grey',
                highlightthickness=0)

_5Button = tkinter.Button(mainWindow, text='5')
_5Button.grid(row=4, column=1, sticky='news')
_5Button.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                highlightcolor='grey',
                highlightbackground='grey',
                highlightthickness=0)

_6Button = tkinter.Button(mainWindow, text='6')
_6Button.grid(row=4, column=2, sticky='news')
_6Button.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                highlightcolor='grey',
                highlightbackground='grey',
                highlightthickness=0)

_minusButton = tkinter.Button(mainWindow, text='-')
_minusButton.grid(row=4, column=3, sticky='news')
_minusButton.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                    highlightcolor='grey',
                    highlightbackground='grey',
                    highlightthickness=0)

_1Button = tkinter.Button(mainWindow, text='1')
_1Button.grid(row=5, column=0, sticky='news')
_1Button.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                highlightcolor='grey',
                highlightbackground='grey',
                highlightthickness=0)

_2Button = tkinter.Button(mainWindow, text='2')
_2Button.grid(row=5, column=1, sticky='news')
_2Button.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                highlightcolor='grey',
                highlightbackground='grey',
                highlightthickness=0)

_3Button = tkinter.Button(mainWindow, text='3')
_3Button.grid(row=5, column=2, sticky='news')
_3Button.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                highlightcolor='grey',
                highlightbackground='grey',
                highlightthickness=0)

_multipleButton = tkinter.Button(mainWindow, text='*')
_multipleButton.grid(row=5, column=3, sticky='news')
_multipleButton.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                       highlightcolor='grey',
                       highlightbackground='grey',
                       highlightthickness=0)

_0Button = tkinter.Button(mainWindow, text='0')
_0Button.grid(row=6, column=0, sticky='news')
_0Button.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                highlightcolor='grey',
                highlightbackground='grey',
                highlightthickness=0)

_equalButton = tkinter.Button(mainWindow, text='=')
_equalButton.grid(row=6, column=1, columnspan=2, sticky='news')
_equalButton.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                    highlightcolor='grey',
                    highlightbackground='grey',
                    highlightthickness=0)

_divButton = tkinter.Button(mainWindow, text='/')
_divButton.grid(row=6, column=3, sticky='news')
_divButton.config(font=buttonFont, relief='flat', activebackground='light blue', justify='center',
                  highlightcolor='grey',
                  highlightbackground='grey',
                  highlightthickness=0)


mainWindow.update()

# if you want to fix the screen size
mainWindow.minsize(inputScreen.winfo_width()+36, inputScreen.winfo_width()+50)
mainWindow.maxsize(inputScreen.winfo_width()+36, inputScreen.winfo_width()+50)
mainWindow.mainloop()
