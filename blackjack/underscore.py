# ===========================================================
# the python import mechanism does actually take note of this convention
# and it won't import any objects that start with an underscore
# with import blackjack you see different list of globals and
# with from blackjack import * you get to see the members of the blackjack module
# ===========================================================
import blackjack  # 1st way of importing the module
# from blackjack import *  # 2nd way on importing the module

# ============================================================
# when executed with the 1st and 2nd way of importing the module you see the difference
# ============================================================
# g = sorted(globals())
# for x in g:
#     print(x)

# ==========================================================
# so if you are using 1st way of importing the module then you can still use the protected member of the imported module
# ==========================================================
# blackjack._deal_card(blackjack.dealer_card_frame)

# ==========================================================
# if you are using the 2nd way of importing the module then you cannot use the protected member of the imported module
# it will give you unresolved reference error.
# ==========================================================
# _deal_card(dealer_card_frame)


# =============================================
# python does not have private or protected member concept
# so anyone can access the function and variables outside of the module
# for e.g

# if you add underscore before the variable name then it becomes protected
# but it still allows you to change the value of the variable.
# we will rename the deal_card to _deal_card
# so after refactoring the function name you can see that it is warning you that
# you are accessing the protected member of the module
# so to be kept in mind, if you find object whose name starts with an underscore then you probably shouldn't
# be doing that the developer of the module has defined it that way for you probably not to access it that way
# =============================================
# blackjack.deal_card(blackjack.dealer_card_frame)
# blackjack._deal_card(blackjack.dealer_card_frame)


# =================================================
# using a double underscore at the start of a name invokes Python's name mangling rules
# which really exists to prevent name clashes

# names that start and end with two underscores
# never try to change the value of the variable starting with two underscores and ending with two underscores
# so in the blackjack module if we define __name__ = '__main__' before declaring the mainWindow variable
# the game is executed but when you close the game you will get error because by closing the game we have destroyed all the tkinter objects
# =================================================


# calling the play function from the module blackjack
blackjack.play()
