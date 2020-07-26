# =================================================================
# three things to be remembered
#   try to write a function so that they only use local variables and parameters only access global and non-local variables
#
# at the module level local scope is same as the global scope so you can see that by printing the locals() and globals()
# =================================================================


# def spam1():
#
#     def spam2():
#
#         def spam3():
#             z = " even"
#             z += y
#             print("In spam3, locals are {}".format(locals()))
#             return z
#
#         y = " more "
#         y += x
#         y += spam3()
#         print("In spam2, locals are {}".format(locals()))
#         return y
#
#     x = "spam"
#     x += spam2()
#     print("In spam1, locals are {}".format(locals()))
#     return x


def spam1():

    def spam2():

        def spam3():
            z = " even"
            z += y
            print("In spam3, locals are {}".format(locals()))
            return z

        y = " more "
        y += x
        y += spam3()
        print("In spam2, locals are {}".format(locals()))
        return y

    '''it will give an error 
    free variable x referenced before assignment in enclosing scope'''
    x = "spam" + spam2()
    print("In spam1, locals are {}".format(locals()))
    return x


print(spam1())
