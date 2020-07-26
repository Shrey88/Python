# =========================================================================================================
# Modify the circle function so that it allows the colour of the circle to be specified
# and defaults to red if a colour is not given.
# Named Parameters and Default Values
# =========================================================================================================
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def draw_axes(canvas_page):
    canvas_page.update()
    x_origin = canvas_page.winfo_width() / 2
    y_origin = canvas_page.winfo_height() / 2
    canvas_page.configure(scrollregion=(-x_origin, -y_origin, 0.0, 0.0))
    canvas_page.create_line(x_origin, 0, -x_origin, 0, fill='red')
    canvas_page.create_line(0, y_origin, 0, -y_origin, fill='blue')


def circle(canvas_page, radius, g, h, colour='green'):
    canvas_page.create_oval(g + radius, -h + radius, g - radius, -h - radius, outline=colour, width=5)


# ============================================
#  Main Block
# ============================================
mainWindow = tkinter.Tk()
mainWindow.title("circle")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)
canvas.config(background='white')

draw_axes(canvas)

circle(canvas, 100, 100, 100, 'yellow')
circle(canvas, 100, 100, -100, 'pink')
circle(canvas, 100, -100, 100, 'purple')
circle(canvas, 100, -100, -100, 'brown')

mainWindow.mainloop()

