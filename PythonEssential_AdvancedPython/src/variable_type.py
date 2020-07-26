""" *
    *
    * """

x = (1, 2, "shrey", [4, 5])
print("Type of X: ", type(x))  # <-- if you print the type of x, it will say class tuple

y = (1, 2, "shrey", [4, 5])  # <-- it is the same tuple as x
print("Type of Y: ", type(y))  # <-- if you print the type of x, it will say class tuple

# but if you print the id of both the variables it will print two different id's which is the unique identifier for each object
print("ID of X : ", id(x))
print("ID of Y : ", id(y))

""" *   if you print the if of the value present at index 0 in typle from both x and y
    *   it will show the same as there is no need to create 2 diff objects for the literal number 1
    * """
print("ID of X[0] : ", id(x[0]))
print("ID of Y[0] : ", id(y[0]))