# ==================================================================================================
# canvas coordinate system has 00 at the top left, whereas a normal graph have the origin 00 in the middle
# shadowing name "variable_name" from outer scope meaning,
# it is using the same variable name which is available in outer scope.
# TO REMEMBER:: a function can use the variables from the main program but the main program cannot see
# variables that are local to the function.
# it is bad idea to to shadow the variables names.
# ==================================================================================================
import math

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


# =================================================
# creating a circle (CUSTOM CODE)
# this is the custom code to plot the circle on canvas
# with the mainWindow being transformed to graph
# as the circles plotted with the first for loop were little bit vague, you can comment that out and uncomment
# the second for loop and the next line after the second for loop
# the performance will be little slower as we are iterating it 100 times.
# =================================================
# def circle(canvas_page, radius, g, h):
#     # for x in range(g, (g + radius)):
#     for x in range(g * 100, (g + radius) * 100):
#         x /= 100
#         y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
#         # print("X: {0} \t Y: {1}".format(x, y))
#         plot(canvas_page, x, y)
#         plot(canvas_page, x, 2 * h - y)
#         plot(canvas_page, 2 * g - x, y)
#         plot(canvas_page, 2 * g - x, 2 * h - y)


# ================================================
# using the canvas method to plot the circle
# canvas widger has a create oval method that can be used to draw circles
#
# ================================================
# def circle(canvas_page, radius, g, h):
#     canvas_page.create_oval(g + radius, -h + radius, g - radius, -h - radius, outline='green', width=2)


# =================================================
# so we are going to comment out the for loop for plotting the parabola
# instead we are going to inherit it in the parabola function itself and call the parabola func by passing the arguments
# as canvas object variable and the size of the parabola
# =================================================
# def parabola(canvas_page, size):
#     for x in range(-size, size):
#         y = (x * x) / size
#         print("X: {0} \t Y: {1}".format(x, y))
#         # here the positive y co-ordinate is opposite to the actual graph plotting on paper i.e. it is pointing downward
#         # where as the negative y co-ordinate is pointing upwards.
#         # plot(canvas_page, x, y)
#
#         # so in case if you want to invert the plotted graph you can change the sign of y to -y.
#         plot(canvas_page, x, -y)


# ================================================
# so here we are going to make some change to the range and plot the negative x in plot function
# ================================================
# def parabola(canvas_page, size):
#     for x in range(size):
#         y = (x * x) / size
#         print("X: {0} \t Y: {1}".format(x, y))
#         # here the positive y co-ordinate is opposite to the actual graph plotting on paper i.e. it is pointing downward
#         # where as the negative y co-ordinate is pointing upwards.
#         # plot(canvas_page, x, y)
#         # plot(canvas_page, -x, y)
#         # so in case if you want to invert the plotted graph you can change the sign of y to -y.
#         plot(canvas_page, x, -y)
#         plot(canvas_page, -x, -y)


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
    # scrollregion => [ left, top, right, bottom ]
    # ==========================================
    canvas_page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas_page.create_line(-x_origin, 0, x_origin, 0, fill='red')
    # canvas_page.create_line(-x_origin//2, -y_origin//2, 0, 0, fill='green')
    canvas_page.create_line(0, y_origin, 0, -y_origin, fill='blue')


# ================================================
# it's drawing a 1 pixel line, basically point
# as tkinter cannot plot points, but it can plot a line between two adjacent pixels.
# you can uncomment it when you want to execute the parabola or custom circle function
# ================================================
# def plot(canvas_page, x, y):
#     canvas_page.create_line(x, y, x + 1, y + 1, fill='green')


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axis(canvas)

# inheriting it in parabola function
# for x in range(-100, 100):
#     y = parabola(x)
#     print("X: {0} \t Y: {1}".format(x, y))
#     # here the positive y co-ordinate is opposite to the actual graph plotting on paper i.e. it is pointing downwards
#     # where as the negative y co-ordinate is pointing upwards.
#     plot(canvas, x, y)
#     # so in case if you want to invert the plotted graph you can change the sign of y to -y.
#     # plot(canvas, x, -y)


# =============================================
# when you want to run the parabola function uncomment the parabola definition
# =============================================
# parabola(canvas, 100)
# parabola(canvas, 200)

# ============================================
# when you want to run the circle function uncomment the circle definition
# ============================================
# circle(canvas, 100, 100, 100)
# circle(canvas, 100, 100, -100)
# circle(canvas, 100, -100, 100)
# circle(canvas, 100, -100, -100)
mainWindow.mainloop()
