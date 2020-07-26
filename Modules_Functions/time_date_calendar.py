# =================================================================================================
# python standard library provides three modules
#   time
#   date-time
#   calendar
# if you are just dealing with elapsed time - like timing how long a program takes to execute
# if you are dealing with actual dates and times then date-time module will be helpful
# the c libraries work by storing the number of seconds since the start date and
# that's referred to generously as the epoc
# ==================================================================================================
import time
# from time import time as my_timer
# from time import perf_counter as my_timer
# from time import monotonic as my_timer
# ===================================================
# amount of time spent on the actual CPU is being recorded
# ===================================================
from time import process_time as my_timer

import random

# =========================================
# below line represents the start of epoc
# =========================================
# print(time.gmtime(0))
#
# print(time.localtime())

# ============================================
# it prints out the number of seconds since
# the start of an epoch that's the number of
# seconds since the first 1970.
# ============================================
# print(time.time())


# ============================================
# print(time.localtime()) gives us the output as named tuple...
# they are just like order tuple, they allow the individual items
# in a tuple to be accessed using a name and that can be very useful
# way to make a code much more readable
# we will assign the current local time to a variable which can be
# tuple and use both methods to access the individual items
# ============================================

# time_here = time.localtime()
# print(time_here)
# print("Year: ", time_here[0], time_here.tm_year)
# print("Month: ", time_here[1], time_here.tm_mon)
# print("Day: ", time_here[3], time_here.tm_mday)


# ============================================
# elapsed time
# ===================================== =======


input("press enter to start")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("press enter to stop")

end_time = my_timer()

print("started at " + time.strftime("%X", time.localtime(start_time)))
print("ended at " + time.strftime("%X", time.localtime(end_time)))


print("your reaction time was {} seconds".format(end_time-start_time))
