# Experiment with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# You may also want to included things like.

# o=range(0, 100, 4)
# print(o)
# p = o[::5]
# print(p)
# for i in p:
#    print(i)
# and see if you can work out what will be printed before running the program. If you are unsure, use a
# for loop to print out the values of o to see why p returns what it does.

o = range(0, 100, 4)
print(o)
for i in o:
   print(i)

# here it prints the values present at 5th index
# again the value from next 5th index
# slicing is done at every 5th index
# for e.g
# 0 4 8 12 16 20  24 28 32 36 40  44 48 52 56 60  64 68 72 76 80
# 0 1 2  3  4 [5]  1  2  3  4 [5]  1  2  3  4 [5]  1  2  3  4 [5]
p = o[::5]
print(p)
for i in p:
   print(i)
