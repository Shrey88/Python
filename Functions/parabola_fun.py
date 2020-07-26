# ==================================================================================================
# canvas coordinate system has 00 at the top left, whereas a normal graph have the origin 00 in the middle
# shadowing name "variable_name" from outer scope meaning,
# it is using the same variable name which is available in outer scope.
# TO REMEMBER:: a function can use the variables from the main program but the main program cannot see
# variables that are local to the function.
# it is bad idea to to shadow the variables names.
# ==================================================================================================
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(x1):
    y1 = x1 * x1 / 100
    return y1


def draw_axis(canvas_page):
    canvas_page.update()  # it forces the canvas to be redrawn
    x_origin = canvas_page.winfo_width() / 2
    y_origin = canvas_page.winfo_height() / 2
    # ==========================================
    # we are shifting the origin from the top left to the middle of the screen,
    # so that (0, 0) now represents a point in the middle
    # here the positive y co-ordinate is opposite to the actual graph plotting on paper i.e. it is pointing downwards
    # where as the negative y co-ordinate is pointing upwards.
    # scroll region is a box and we specify 2 pairs of points for the opposite corners of the box.
    # ==========================================
    canvas_page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))  #
    canvas_page.create_line(-x_origin, 0, x_origin, 0, fill='red')
    # canvas_page.create_line(-x_origin//2, -y_origin//2, 0, 0, fill='green')
    canvas_page.create_line(0, y_origin, 0, -y_origin, fill='blue')


# ================================================
# it's drawing a 1 pixel line, basically point
# as tkinter cannot plot points, but it can plot a line between two adjacent pixels.
# ================================================
def plot(canvas_page, x1, y1):
    canvas_page.create_line(x1, y1, x1 + 1, y1 + 1, fill='green')


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axis(canvas)


for x in range(-100, 100):
    y = parabola(x)
    print("X: {0} \t Y: {1}".format(x, y))
    # here the positive y co-ordinate is opposite to the actual graph plotting on paper i.e. it is pointing downwards
    # where as the negative y co-ordinate is pointing upwards.
    plot(canvas, x, y)
    # so in case if you want to invert the plotted graph you can change the sign of y to -y.
    # plot(canvas, x, -y)

mainWindow.mainloop()
