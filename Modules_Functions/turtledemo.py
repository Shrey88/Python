# ===========================================
# turtle module is based on the educational programming language from 1960's called MSWLogo
# ===========================================
import turtle

# ===========================================
# another way of importing the module
# here you are mentioning which methods/functions you want to import.
# ===========================================
# from turtle import right, forward, done

# ===========================================
# another way of importing the module
# here you are trying to import all the methods/functions. (NOT RECOMMENDED)
# it will override the your variable with the method defined in the module.
# ===========================================
# from turtle import *

# ===================================
# we can make use of the time module to hold the screen for few sec
# ===================================
import time

# ========================================
# the below line should suppress the warnings related to the forward, right...
# it suppresses the warning message only for the very next line to it.
# so to remove it from all the turtle functions click on the function name were the warning is still their
# so you will get the bulb sign --> select the option "Mark all unresolved attributes of 'turtle' as ignored"
# ========================================
# noinspection PyUnresolvedReferences
turtle.forward(150)
turtle.right(240)
turtle.forward(150)
turtle.right(240)
turtle.forward(150)
turtle.circle(75)
# ========================================
# when you are using the second method of defining the module
# you can actually avoid writing turtle.
# ========================================
# forward(150)
# right(240)
# forward(150)
# right(240)
# forward(150)
# circle(75)


# time.sleep(4)
# ===============================
# with these option the window will still remain open until and unless you explicitly click on the cross button
# ===============================
turtle.done()
