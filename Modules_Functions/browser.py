# =====================================
# understand the webbrowser module
# =====================================
import webbrowser

# to open any link in the default browser
# webbrowser.open("https://www.python.org/")

#help(webbrowser)

# =========================================
# getting the controller of the webbrowser
# =========================================
# chrome = webbrowser.get(using='windows-default')
# chrome.open_new("https://www.python.org/")


# =====================================
# another way of getting the controller of webbrowser
# and opening it
# =====================================
chrome = webbrowser.get(using='windows-default').open_new_tab("https://www.python.org/")
