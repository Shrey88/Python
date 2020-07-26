# ===========================================================================================
# here we are trying to import the blackjack program as module
# but when we import the blackjack and execute it, it runs the blackjack program.
# so we are interested in not running the game automatically and only want it to run when we ask for it.
# ===========================================================================================
import blackjack


# ===========================================
# this is the attribute of the module (is set to be file name without extension)
# so to prevent the module to execute automatically, we can control it with the help of this attribute
# in both the places i.e in the module file itself as well in the calling file.
# so after putting if condition for checking if the value of attribute of the module is "__main__" or not
# depending on that module will get executed
# ===========================================
print(__name__)


# calling the play function from the module blackjack
blackjack.play()



